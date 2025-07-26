from django.urls import path
from .api import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product_list_create'),
    path('products/<slug:slug>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
]
