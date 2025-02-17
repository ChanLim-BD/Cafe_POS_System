from pydantic import BaseModel
from datetime import date, datetime
from decimal import Decimal

class ProductBase(BaseModel):
    category: str
    price: Decimal
    cost: Decimal
    name: str
    description: str
    barcode: str
    expiration_date: date
    size: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        orm_mode = True  # ORM 모델과 호환되도록 설정

class UserResponse(BaseModel):
    id: int
    phone_number: str
    name: str
    date_joined: datetime

    class Config:
        orm_mode = True
