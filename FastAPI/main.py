from fastapi import FastAPI
from db.models import Base
from db.database import engine
from routes import user  # User API 라우터
from utils.common import lifespan

app = FastAPI(lifespan=lifespan)

# DB 테이블 생성 (비동기 방식으로 처리)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# 테이블 생성 (비동기 작업)
async def on_startup():
    await create_tables()

# User API 라우터 등록
app.include_router(user.router)

# 기본 엔드포인트
@app.get("/")
def read_root():
    return {"message": "FastAPI User API"}
