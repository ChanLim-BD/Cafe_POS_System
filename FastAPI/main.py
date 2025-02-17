from fastapi import FastAPI
from routes import user, product
from utils.common import lifespan

app = FastAPI(lifespan=lifespan)

# User API 라우터 등록
app.include_router(user.router)
app.include_router(product.router)

# 기본 엔드포인트
@app.get("/")
def read_root():
    return {"message": "FastAPI User API"}
