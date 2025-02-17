from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Product
from schemas.product_schema import ProductCreate, ProductResponse
from typing import Optional, List


async def get_product_all(db: AsyncSession) -> List[ProductResponse]:
    result = await db.execute(select(Product))
    all_products = [
        ProductResponse.from_orm(row)  # Product 객체에서 직접 ProductResponse를 생성
        for row in result.scalars()  # .scalars()를 사용하여 실제 데이터만 추출
    ]
    return all_products



async def get_product(db: AsyncSession, product_id: int) -> Optional[ProductResponse]:
    result = await db.execute(select(Product).filter(Product.id == product_id))
    return result.scalars().first()

async def create_product(db: AsyncSession, product: ProductCreate, owner_id: int) -> Product:
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
