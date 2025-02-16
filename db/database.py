import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# database connection URL
load_dotenv()
DATABASE_CONN = os.getenv("DATABASE_CONN")
"""
DATABASE_CONN=mysql+aiomysql://{사용자이름}:{비밀번호}@{DB의IP:PORT}/{테이블명}
"""

"""비동기 방식"""
engine: AsyncEngine = create_async_engine(DATABASE_CONN, #echo=True,
                    #   poolclass=QueuePool,
                    #   poolclass=NullPool, # Connection Pool 사용하지 않음. 
                       pool_size=10, max_overflow=0,
                       pool_recycle=300)


# 엔진 생성
engine_orm = create_async_engine(DATABASE_CONN, echo=True)

# 세션 로컬 생성
AsyncSessionLocal = sessionmaker(
    engine_orm,
    expire_on_commit=False,
    class_=AsyncSession
)
# 모델의 기본 클래스 생성
Base = declarative_base()

# 데이터베이스 세션을 얻기 위한 의존성
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session