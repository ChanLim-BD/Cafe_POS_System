from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.product_schema import ProductBase, ProductCreate, ProductResponse
from service.product_svc import create_product, get_product, get_product_all, edit_product, remove_product
from service.user_svc import get_current_user_id
from db.database import get_db

router = APIRouter()

@router.get("/products")
async def read_all_products(db: AsyncSession = Depends(get_db), owner_id: int = Depends(get_current_user_id)):
    db_product = await get_product_all(db)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="상품이 존재하지 않습니다.")
    return db_product


@router.get("/products/{product_id}")
async def read_product(product_id: int, db: AsyncSession = Depends(get_db), owner_id: int = Depends(get_current_user_id)):
    db_product = await get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="상품이 존재하지 않습니다.")
    return db_product


@router.post("/products/create", response_model=ProductResponse)
async def create_new_product(product: ProductCreate, db: AsyncSession = Depends(get_db), owner_id: int = Depends(get_current_user_id)):
    db_product = await create_product(db, product, owner_id)
    return db_product


@router.post("/products/{product_id}/update", response_model=ProductBase)
async def update_product(product_id: int, product: ProductBase, db: AsyncSession = Depends(get_db), owner_id: int = Depends(get_current_user_id)):
    db_product = await edit_product(db, product_id, product)
    return db_product


@router.post("/products/{product_id}/delete")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db), owner_id: int = Depends(get_current_user_id)):
    db_product = await remove_product(db, product_id)
    return db_product