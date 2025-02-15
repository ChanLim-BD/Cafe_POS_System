from django.urls import path
from products.views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),  # 내 상품 조회
    path("create/", ProductCreateView.as_view(), name="product-create"),  # 상품 등록
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),  # 수정/삭제/조회
]
