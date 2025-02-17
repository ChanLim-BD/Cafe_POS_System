from contextlib import asynccontextmanager
from db.database import engine
from db.models import Base

# DB 테이블 생성 (비동기 방식으로 처리)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# FastAPI lifespan 설정
@asynccontextmanager
async def lifespan(app):
    # FastAPI 인스턴스 기동시 필요한 작업 수행
    print("Starting up...")
    
    # 테이블 생성
    await create_tables()

    yield  # 애플리케이션의 라이프 사이클

    # FastAPI 인스턴스 종료시 필요한 작업 수행
    print("Shutting down...")
    await engine.dispose()  # 연결 종료
