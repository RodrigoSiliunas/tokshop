from typing import Optional

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from fastapi.param_functions import Body

from sqlmodel import Session, select
from pydantic import BaseModel


from app.models import (
    User,
    Product
)
from app.packages.Auth import (
    get_current_user,
    is_user_administrator,
)
from app.configurations.database import engine


class ProductCreate(BaseModel):
    image: Optional[str]
    name: str
    description: str
    price: float | int
    height: float | int


router = APIRouter(prefix="/v1")


@router.get('/products')
async def get_all_products(user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        query = select(Product)
        products = session.exec(query).all()

        return JSONResponse({"products": products})



@router.get('/products/{id}')
async def get_product(id: int, user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        query = select(Product).where(Product.id == id)
        product = session.exec(query).first()

        if not product:
            raise HTTPException({
                "error": {
                    "message": f"No product with identifier {id} was found.",
                    "type": "ProductError",
                    "code": 404
                }
            }, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse({"product": product})


@router.post('/products')
async def create_product(
        product: ProductCreate = Body(...), user: User = Depends(is_user_administrator)) -> JSONResponse:
    with Session(engine) as session:
        new_product = Product(**product.dict())

        session.add(new_product)
        session.commit()

        return JSONResponse({
            "success": {
                "message": "Product created successfully",
                "type": "ProductInfo",
                "code": status.HTTP_201_CREATED
            }
        }, status.HTTP_201_CREATED)



@router.patch('/products/{id}')
async def update_product(
        id: int, product: ProductCreate, user: User = Depends(is_user_administrator)) -> JSONResponse:
    with Session(engine) as session:
        query = select(Product).where(Product.id == id)
        existing_product = session.exec(query).first()

        if not existing_product:
            raise HTTPException({
                "error": {
                    "message": f"No product with identifier {id} was found.",
                    "type": "ProductError",
                    "code": 404
                }
            }, status_code=status.HTTP_404_NOT_FOUND)

        existing_product.image = product.image
        existing_product.name = product.name
        existing_product.description = product.description
        existing_product.price = product.price
        existing_product.height = product.height

        session.commit()

        return JSONResponse({
            "success": {
                "message": "Product updated successfully",
                "type": "ProductInfo",
                "code": status.HTTP_200_OK
            }
        }, status.HTTP_200_OK)


@router.delete('/products/{id}')
async def delete_product(
        id: int, user: User = Depends(is_user_administrator)) -> JSONResponse:
    with Session(engine) as session:
        query = select(Product).where(Product.id == id)
        existing_product = session.exec(query).first()

        if not existing_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        session.delete(existing_product)
        session.commit()

        return JSONResponse({
            "success": {
                "message": "Product deleted successfully",
                "type": "ProductInfo",
                "code": status.HTTP_200_OK
            }
        }, status.HTTP_200_OK)
