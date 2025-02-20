import factory
from faker import Faker
from decimal import Decimal
from products.models import Product
from accounts.tests.factories import UserFactory  # UserFactory 임포트

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    # UserFactory로 생성된 User 객체를 owner로 지정
    owner = factory.SubFactory(UserFactory)

    category = factory.Faker("word")  # 카테고리는 임의로 단어 생성
    price = factory.LazyAttribute(lambda _: Decimal(fake.random_number(digits=5)))  # 가격은 5자리 랜덤 숫자
    cost = factory.LazyAttribute(lambda _: Decimal(fake.random_number(digits=4)))  # 원가는 4자리 랜덤 숫자
    name = factory.Faker("word")  # 이름은 임의로 단어 생성
    description = factory.Faker("text")  # 설명은 임의로 긴 텍스트 생성
    barcode = factory.Faker("ean13")  # EAN13 바코드 형식으로 생성
    expiration_date = factory.Faker("date_this_year")  # 만료일은 올해의 날짜 중 하나로 생성
    size = factory.Faker("random_element", elements=["small", "large"])  # 사이즈는 'small' 또는 'large' 중 하나
