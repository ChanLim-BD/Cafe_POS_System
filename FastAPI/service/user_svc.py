from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from utils.fast_jwt import verify_jwt_token  # JWT 토큰 검증 함수

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="로그인 정보가 필요합니다.")
    
    # 토큰 검증
    user_data = verify_jwt_token(token)  # 토큰 검증하는 함수 사용
    return user_data

