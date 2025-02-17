from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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
