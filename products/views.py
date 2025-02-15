from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    상품을 등록/조회/수정/삭제하는 API
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        현재 로그인한 사용자가 등록한 상품만 조회
        """
        return Product.objects.all()

    def perform_create(self, serializer):
        """
        상품 등록 시 현재 로그인한 사용자를 owner로 지정
        """
        serializer.save(owner=self.request.user)
