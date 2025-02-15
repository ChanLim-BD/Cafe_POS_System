from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone number field must be set")
        if not name:
            raise ValueError("The Name field must be set")

        # 사용자 모델 생성
        user = self.model(phone_number=phone_number, name=name, **extra_fields)
        user.set_password(password)  # 비밀번호 해싱 처리
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        return self.create_user(phone_number, name, password, **extra_fields)
