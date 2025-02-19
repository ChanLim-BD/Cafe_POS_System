from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from products.models import Product
from products.serializers import ProductSerializer
from products.utils import get_initial_consonant



class ProductViewSet(viewsets.ModelViewSet):
    """
    상품을 등록/조회/수정/삭제하는 API
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs): 
        try:
            # 기본 list 응답을 호출
            response = super().list(request, *args, **kwargs) 

            # 응답 데이터 구조 수정
            if isinstance(request.accepted_renderer, (JSONRenderer, BrowsableAPIRenderer)): 
                response.data = {
                    "head": {
                        "code": 200,                # HTTP 상태 코드
                        "message": "ok"             # 메시지
                    },
                    "data": {
                        "products": response.data  # 실제 상품 데이터
                    }
                }
            return response
        except Exception as e:
            # 예외 발생 시 400 Bad Request 응답
            return Response({
                "head": {
                    "code": 400,
                    "message": str(e)  # 에러 메시지 전달
                },
                "data": None  # 데이터는 null로 설정
            }, status=400)



    def get_queryset(self):
        """
        현재 로그인한 사용자가 등록한 상품만 조회
        """
        queryset = Product.objects.all()
        search_query = self.request.query_params.get("search", None)

        if search_query:
            for product in queryset:
                """
                DB의 Product 객체의 name -> 초성 추출
                """
                initial_consonant = get_initial_consonant(product.name)
                """
                검색 초성이 추출 초성에 포함된 경우 : 완료
                """
                if search_query in initial_consonant:
                    search_query = product.name
                    break

            queryset = queryset.filter(Q(name__icontains=search_query))

        return queryset

    def perform_create(self, serializer):
        """
        상품 등록 시 현재 로그인한 사용자를 owner로 지정
        """
        serializer.save(owner=self.request.user)
