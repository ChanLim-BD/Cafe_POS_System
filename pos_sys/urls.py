from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")), # auth 테스트
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
]
