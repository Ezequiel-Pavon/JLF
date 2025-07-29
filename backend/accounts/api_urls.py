from django.urls import path
from .api import ProductListCreate, ProductRetrieveUpdateDestroy, ServiceListCreateAPI, ServiceDetailAPI

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product_list_create'),
    path('products/<slug:slug>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('services/', ServiceListCreateAPI.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceDetailAPI.as_view(), name='service-detail'),
]
