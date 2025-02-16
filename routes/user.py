from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext

from db.models import User
from db.database import get_db
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해싱 함수
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# 회원가입 엔드포인트 (비동기)
@router.post("/", response_model=UserResponse)
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
