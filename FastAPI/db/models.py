from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(15), unique=True, index=True, nullable=False)  # 길이 15로 설정
    name = Column(String(255), nullable=False)  # 길이 255로 설정 (기본적으로 많이 사용됨)
    hashed_password = Column(String(200), nullable=False)  # 비밀번호 해싱하여 저장
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    date_joined = Column(DateTime, default=datetime.now)

    products = relationship("Product", back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, phone_number={self.phone_number}, name={self.name})>"
    


class Product(Base):
    __tablename__ = "products"
    
    SIZE_CHOICES = [("small", "Small"), ("large", "Large")]

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))  # User 모델과 관계 설정
    category = Column(String(50))
    price = Column(Integer)
    cost = Column(Integer)
    name = Column(String(100))
    description = Column(String(255))
    barcode = Column(String(30), unique=True)
    expiration_date = Column(Date)
    size = Column(String(10))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="products")  # 사용자와 관계 설정

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, category={self.category})>"