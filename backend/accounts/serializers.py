# accounts/serializers.py
from django.core.files.storage import default_storage
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Product

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
    
class ProductSerializer(serializers.ModelSerializer):
    # Este campo se usará para devolver las URLs absolutas
    images = serializers.SerializerMethodField()
    features = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = Product
        fields = ['slug', 'name', 'category', 'description', 'features', 'images']

    def get_images(self, obj):
        """
        Devuelve una lista de URLs absolutas a las imágenes,
        p. ej. 'http://localhost:8000/media/...'
        """
        request = self.context.get('request')
        return [
            request.build_absolute_uri(path)
            for path in obj.images
        ]

    def create(self, validated_data):
        # Extraer los archivos subidos
        image_files = validated_data.pop('images', [])

        # Crear el producto sin imágenes
        product = Product.objects.create(**validated_data)

        # Guardar físicamente cada archivo y recoger su URL
        urls = []
        for img in image_files:
            path = f'products/{product.slug}/{img.name}'
            saved_path = default_storage.save(path, img)
            urls.append(default_storage.url(saved_path))

        # Asignar la lista de URLs al JSONField y guardar
        product.images = urls
        product.save()

        return product
