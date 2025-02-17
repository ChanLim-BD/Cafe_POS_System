from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Product
from schemas.product_schema import ProductCreate
from typing import Optional

async def get_product(db: AsyncSession, product_id: int) -> Optional[Product]:
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
