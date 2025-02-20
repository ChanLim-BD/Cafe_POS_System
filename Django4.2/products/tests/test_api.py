import base64

import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from accounts.models import User
from accounts.tests.factories import UserFactory
from products.models import Product
from products.tests.factories import ProductFactory


def create_user(raw_password: str = None) -> User:
    """새로운 User 레코드를 생성 및 반환"""
    return UserFactory(raw_password=raw_password)


@pytest.fixture
def unauthenticated_api_client() -> APIClient:
    """Authorization 인증 헤더가 없는 기본 APIClient 인스턴스 반환"""
    return APIClient()


@pytest.fixture
def api_client_with_new_user_basic_auth(faker) -> APIClient:
    """새로운 User 레코드를 생성하고, 그 User의 인증 정보가 Authorization 헤더로 지정된 APIClient 인스턴스 반환"""
    raw_password: str = faker.password()

    # 사용자 생성
    user: User = create_user(raw_password)
    
    # 생성된 사용자 확인을 위한 로깅
    print(f"Created user: {user.phone_number}, password: {raw_password}")

    client = APIClient()

    # login 시 phone_number 사용
    api_client = client.login(username=user.phone_number, password=raw_password)

    if api_client:
        print(f"APIClient logged in successfully with phone_number: {user.phone_number}")
    else:
        print(f"Failed to login with phone_number: {user.phone_number}")
    
    # 생성된 APIClient에서 Authorization 헤더를 출력하여 확인
    print(f"APIClient Authorization header: {client.defaults.get('HTTP_AUTHORIZATION')}")

    return client



@pytest.fixture
def new_user() -> User:
    """새로운 User 레코드를 생성 및 반환"""
    return create_user()


@pytest.fixture
def new_product() -> Product:
    """새로운 Post 레코드를 반환"""
    return ProductFactory()



@pytest.mark.it("인증하지 않은 요청은 상품 조회 거부")
@pytest.mark.django_db
def test_unauthenticated_user_product_list(unauthenticated_api_client):
    url = reverse("api-v1:product-list")
    response: Response = unauthenticated_api_client.get(url)
    assert status.HTTP_403_FORBIDDEN == response.status_code



@pytest.mark.it("인증된 요청은 상품 조회 요청 성공")
@pytest.mark.django_db
def test_authenticated_user_can_list_product(api_client_with_new_user_basic_auth):
    product_list = [ProductFactory() for __ in range(10)]

    url = reverse("api-v1:product-list")
    response: Response = api_client_with_new_user_basic_auth.get(url)
    assert status.HTTP_200_OK == response.status_code