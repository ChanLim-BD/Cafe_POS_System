from fastapi import FastAPI
from routes import user  # User API 라우터
from utils.common import lifespan

app = FastAPI(lifespan=lifespan)

# User API 라우터 등록
app.include_router(user.router)

# 기본 엔드포인트
@app.get("/")
def read_root():
    return {"message": "FastAPI User API"}
