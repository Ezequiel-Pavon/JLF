from django.contrib import admin
from django.urls import path, include
from accounts.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('accounts.api_urls')),  # endpoints CRUD de productos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)