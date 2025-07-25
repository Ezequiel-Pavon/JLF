# accounts/api.py
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class ProductListCreate(generics.ListCreateAPIView):
    """
    GET: lista pública de productos (AllowAny)
    POST: solo admin (IsAdmin)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [IsAdmin()]

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: detalle público (AllowAny)
    PUT/PATCH/DELETE: solo admin (IsAdmin)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [IsAdmin()]
