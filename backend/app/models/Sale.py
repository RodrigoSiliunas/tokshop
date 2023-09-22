from datetime import datetime
from typing import Optional
from pydantic import condecimal
from sqlmodel import SQLModel, Relationship, Field

from app.models import (
    User,
    Product
)

class Sale(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, unique=True)

    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id")

    price: condecimal(decimal_places=2) = Field(default=0)
    weight: condecimal(decimal_places=2) = Field(default=0)
    quantity: int

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="sales")
    product: Optional[Product] = Relationship(back_populates="sales")
