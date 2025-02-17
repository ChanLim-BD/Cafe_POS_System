from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Product
from schemas.product_schema import ProductCreate, ProductResponse
from typing import Optional, List


async def get_product_all(db: AsyncSession) -> List[ProductResponse]:
    try:
        result = await db.execute(select(Product))
        all_products = [
            ProductResponse.model_validate(row)  # Product 객체에서 직접 ProductResponse를 생성
            for row in result.scalars()  # .scalars()를 사용하여 실제 데이터만 추출
        ]
        return all_products
    
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="요청하신 서비스가 잠시 내부적으로 문제가 발생하였습니다.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="알수없는 이유로 서비스 오류가 발생하였습니다")


async def get_product(db: AsyncSession, product_id: int) -> Optional[ProductResponse]:
    try:
        result = await db.execute(select(Product).filter(Product.id == product_id))
        return result.scalars().first()
    
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="요청하신 서비스가 잠시 내부적으로 문제가 발생하였습니다.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="알수없는 이유로 서비스 오류가 발생하였습니다")


async def create_product(db: AsyncSession, product: ProductCreate, owner_id: int) -> Product:
    try:
        db_product = Product(
            owner_id=owner_id,
            category=product.category,
            price=product.price,
            cost=product.cost,
            name=product.name,
            description=product.description,
            barcode=product.barcode,
            expiration_date=product.expiration_date,
            size=product.size
        )
        db.add(db_product)
        await db.commit()
        await db.refresh(db_product)
        return db_product
    
    except SQLAlchemyError as e:
        print(e)
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="요청데이터가 제대로 전달되지 않았습니다.")