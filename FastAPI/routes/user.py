import os, jwt

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates
from db.models import User
from db.database import get_db
from schemas.user_schema import UserCreate, UserResponse, UserLogin, Token
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# SECRET_KEY = "your_secret_key"  # 보안을 위해 환경변수에서 관리
# ALGORITHM = ""
# ACCESS_TOKEN_EXPIRE_MINUTES = 30 

router = APIRouter(prefix="/users", tags=["Users"])
templates = Jinja2Templates(directory="templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해싱 함수
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# JWT 토큰 생성 함수
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.get("/register")
async def register_user_ui(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register_user.html",
        context={}
    )


# 회원가입 엔드포인트 (비동기)
@router.post("/register", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    # 이미 존재하는 전화번호인지 확인 (비동기)
    result = await db.execute(select(User).filter(User.phone_number == user_data.phone_number))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 등록된 번호입니다.")

    # 새로운 사용자 생성
    new_user = User(
        phone_number=user_data.phone_number,
        name=user_data.name,
        hashed_password=hash_password(user_data.password),
    )

    db.add(new_user)

    # 비동기 커밋
    await db.commit()

    # 비동기 리프레시 (새로 추가된 사용자 객체를 DB에서 가져오고 최신 상태로 갱신)
    await db.refresh(new_user)
    
    return new_user


@router.get("/login")
async def login_ui(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


# 로그인 엔드포인트
@router.post("/login", response_model=Token)
async def login_user(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    # 사용자 정보 조회 (전화번호)
    result = await db.execute(select(User).filter(User.phone_number == user_data.phone_number))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="전화번호 또는 비밀번호가 일치하지 않습니다.")

    # 비밀번호 검증
    is_correct_pw = verify_password(plain_password=user_data.password, hashed_password=user.hashed_password)
    if not is_correct_pw:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="등록하신 전화번호와 패스워드 정보가 입력 정보와 다릅니다.")
    
    # JWT 토큰 생성
    access_token = create_access_token(data={"sub": user.phone_number})
    
    # JWT 토큰과 사용자 정보를 함께 반환
    response_data = {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserResponse.model_validate(user)  # 사용자 정보 포함
    }

    return response_data