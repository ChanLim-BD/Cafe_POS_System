from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

# DefaultRouter 생성
router = DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),  # DefaultRouter에 등록된 모든 URL 포함
]