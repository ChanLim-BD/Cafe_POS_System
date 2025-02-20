from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

# DefaultRouter 생성
router = DefaultRouter()
router.register(prefix="products", viewset=ProductViewSet, basename='product')

urlpatterns = []
urlpatterns_api_v1 = []
urlpatterns_api_v1 += router.urls


urlpatterns += [
    path("api/", include((urlpatterns_api_v1, "api-v1"))),
]