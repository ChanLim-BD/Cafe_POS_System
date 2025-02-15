from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializer


# 상품 등록 (POST)
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # 현재 로그인한 사용자를 owner로 저장


# 상품 리스트 조회 (GET)
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)  # 본인이 등록한 상품만 조회


# 상품 부분 수정 (PATCH) & 상세 조회 (GET)
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # 로그인 필수 
