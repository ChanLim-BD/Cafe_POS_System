from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from accounts.managers import UserManager

phone_number_validator = RegexValidator(
    regex=r'^(01[0-9])\d{7,8}$',
    message="휴대폰 번호는 010, 011, 016, 017, 018, 019 등으로 시작하고, 숫자가 8~9자리이어야 합니다."
)

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True,
        validators=[phone_number_validator]  # 휴대폰 번호 유효성 검사를 추가
    )
    name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"  # 기본 사용자 이름 필드를 phone_number 설정
    REQUIRED_FIELDS = ["name"]  # 비어 있어도 되지만, 만약 추가 필드가 필요하다면 여기에 지정

    def __str__(self):
        return self.name