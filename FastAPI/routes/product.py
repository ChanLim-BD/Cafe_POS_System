from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.product_schema import ProductCreate, ProductResponse
from service.product_svc import create_product, get_product
from service.user_svc import get_current_user_id
from db.database import get_db

router = APIRouter()

@router.post("/products/create", response_model=ProductResponse)
async def create_new_product(product: ProductCreate, db: AsyncSession = Depends(get_db), owner_id: int = Depends(get_current_user_id)):
    db_product = await create_product(db, product, owner_id)
    return db_product


@router.get("/products/{product_id}", response_model=ProductResponse)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="상품이 존재하지 않습니다.")
    return db_product
