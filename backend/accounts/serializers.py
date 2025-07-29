# accounts/serializers.py
from django.core.files.storage import default_storage
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Product, Service

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
    
class ProductSerializer(serializers.ModelSerializer):
    # → Read‑only URLs
    images = serializers.SerializerMethodField()
    # → Write‑only uploaded files
    images_upload = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    features = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = Product
        fields = [
            'slug','name','category','description',
            'features','images','images_upload'
        ]

    def get_images(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(path) for path in obj.images]

    def _save_files(self, slug, files, subdir):
        urls = []
        for img in files:
            path = f'{subdir}/{slug}/{img.name}'
            saved = default_storage.save(path, img)
            urls.append(default_storage.url(saved))
        return urls

    def create(self, validated_data):
        uploads = validated_data.pop('images_upload', [])
        product = Product.objects.create(**validated_data)
        urls = self._save_files(product.slug, uploads, 'products')
        product.images = urls
        product.save()
        return product

    def update(self, instance, validated_data):
        uploads = validated_data.pop('images_upload', [])
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        # Añadimos las nuevas, sin borrar las viejas
        urls = list(instance.images or [])
        urls += self._save_files(instance.slug, uploads, 'products')
        instance.images = urls
        instance.save()
        return instance


class ServiceSerializer(serializers.ModelSerializer):
    # → Read‑only URLs
    images = serializers.SerializerMethodField()
    # → Write‑only uploads
    images_upload = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    features = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = Service
        fields = [
            'slug','title','description',
            'features','images','images_upload',
            'created_at','updated_at'
        ]
        read_only_fields = ['created_at','updated_at']

    def get_images(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(path) for path in obj.images]

    def _save_files(self, slug, files):
        urls = []
        for img in files:
            path = f'services/{slug}/{img.name}'
            saved = default_storage.save(path, img)
            urls.append(default_storage.url(saved))
        return urls

    def create(self, validated_data):
        uploads = validated_data.pop('images_upload', [])
        service = Service.objects.create(**validated_data)
        service.images = self._save_files(service.slug, uploads)
        service.save()
        return service

    def update(self, instance, validated_data):
        uploads = validated_data.pop('images_upload', [])
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        urls = list(instance.images or [])
        urls += self._save_files(instance.slug, uploads)
        instance.images = urls
        instance.save()
        return instance