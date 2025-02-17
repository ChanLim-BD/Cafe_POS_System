from pydantic import BaseModel, field_validator
import re


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
        orm_mode = True  # SQLAlchemy 모델을 Pydantic으로 변환할 때 필요

