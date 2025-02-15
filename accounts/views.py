from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.models import User
from accounts.serializers import UserSignupSerializer


class UserSignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "회원가입이 완료되었습니다!", "user": response.data},
            status=status.HTTP_201_CREATED
        )
