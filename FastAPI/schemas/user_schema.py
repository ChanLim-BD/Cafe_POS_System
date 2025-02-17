import re
from pydantic import BaseModel, field_validator


class UserCreate(BaseModel):
    phone_number: str
    name: str
    password: str  # 비밀번호를 평문으로 받음

    @field_validator('phone_number')
    def validate_phone_number(cls, v):
        if not re.match(r'^(01[0-9])\d{7,8}$', v):
            raise ValueError('Invalid phone number format')
        return v

class UserResponse(BaseModel):
    id: int
    phone_number: str
    name: str
    is_active: bool
    is_staff: bool
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    phone_number: str
    password: str


# 로그인 성공 시 반환할 토큰 모델
class Token(BaseModel):
    access_token: str
    token_type: str