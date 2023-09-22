from datetime import datetime
from pydantic import condecimal
from sqlmodel import SQLModel, Relationship, Field


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, unique=True)

    name: str
    description: str
    price: condecimal(decimal_places=2) = Field(default=0)
    weight: condecimal(decimal_places=2) = Field(default=0)
    quantity: int

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    users: list["UserProduct"] = Relationship(back_populates="product")
    sales: list["Sale"] = Relationship(back_populates="product")
