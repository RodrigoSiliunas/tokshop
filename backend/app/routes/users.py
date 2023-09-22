from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.param_functions import Body
from fastapi.responses import JSONResponse

from sqlmodel import Session, select
from pydantic import BaseModel

from app.configurations.database import engine
from app.models import (
    User,
    UserProduct,
    Product,
    UserProduct
)
from app.packages.Auth import (
    get_current_user,
    is_user_administrator
)


class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str


router = APIRouter(prefix="/v1")


@router.get('/users/me')
async def get_me(user: User = Depends(get_current_user)) -> JSONResponse:
    user_data = {
        "id": user.id,
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "type": user.type
    }

    return JSONResponse({
        "user": user_data
    }, status.HTTP_200_OK)


@router.get('/users/{id}')
async def get_user_by_id(
        id: str, user: User = Depends(is_user_administrator)) -> JSONResponse:
    with Session(engine) as session:
        query = select(User).where(User.id == id)
        user = session.exec(query).first()

        if not user:
            raise HTTPException(detail={
                "error": {
                    "message": "User not found error.",
                    "type": "UserError",
                    "code": 404
                }
            }, status_code=status.HTTP_404_NOT_FOUND)

        return JSONResponse({
            "user": user
        }, status.HTTP_200_OK)


@router.get('/users')
async def get_users(user: User = Depends(is_user_administrator)) -> JSONResponse:
    with Session(engine) as session:
        query = select(User)
        users = session.exec(query).all()
        users_count = len(users)

        return JSONResponse({
            "users": users,
            "users_count": users_count
        }, status.HTTP_200_OK)


@router.get('/users/products')
async def get_user_products(user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        # Obter os produtos associados ao usuário
        query = select(UserProduct).where(UserProduct.user_id == user.id)
        user_products = session.exec(query).all()

        # Montar a lista de produtos
        products = []
        for user_product in user_products:
            product = session.get(Product, user_product.product_id)
            products.append(product)

        return JSONResponse({
            "user_id": user.id,
            "products": products
        })


@router.post('/users')
async def create_user(user: UserCreate = Body(...)) -> JSONResponse:
    # Verificar se o email já não existe em nossa base de dados.
    with Session(engine) as session:
        query = select(User).where(User.email == user.email)
        existing_user = session.exec(query).first()

        if existing_user:
            raise HTTPException(detail={
                "error": {
                    "message": "There is already a user with an active registration using the same email. If you forgot your password, try to recover it.",
                    "type": "UserError",
                    "code": 409
                }
            }, status_code=status.HTTP_409_CONFLICT)

        new_user = User(**user.dict())
        new_user.set_password(user.password)

        session.add(new_user)
        session.commit()

    # TODO: Enviar email de confirmação para email informado em Body.

    # Retorno do usuário criado (ou qualquer outra resposta desejada):
    return JSONResponse({
        "success": {
            "message": "You have been successfully created a new account. Please confirm your account in the email we just sent you and log in.",
            "type": "UserInfo",
            "code": 201
        }
    }, status.HTTP_201_CREATED)


@router.patch('/users')
async def update_user(
        updated_user: UserCreate, current_user: User = Depends(get_current_user)) -> JSONResponse:
    with Session(engine) as session:
        # Verificar se o email já não existe em nossa base de dados.
        query = select(User).where(User.email == updated_user.email)
        existing_user = session.exec(query).first()

        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(detail={
                "error": {
                    "message": "There is already a user with an active registration using the same email. If you forgot your password, try to recover it.",
                    "type": "UserError",
                    "code": 409
                }
            }, status_code=status.HTTP_409_CONFLICT)

        # Atualizar as informações do usuário
        current_user.name = updated_user.name
        current_user.username = updated_user.username
        current_user.email = updated_user.email
        current_user.set_password(updated_user.password)

        session.add(current_user)
        session.commit()

        return JSONResponse({
            "success": {
                "message": "User information updated successfully.",
                "type": "UserInfo",
                "code": 200
            }
        }, status.HTTP_200_OK)


@router.delete('/users/{id}')
async def delete_user(id: int, user: User = Depends(is_user_administrator)):
    with Session(engine) as session:
        user_by_id = session.get(User, id)
        if user_by_id:
            session.delete(user_by_id)
            session.commit()
            return JSONResponse({
                "success": {
                    "message": f"User with identifier {id} successfully deleted.",
                    "type": "UserInfo",
                    "code": 200
                }
            }, status.HTTP_200_OK)
        else:
            raise HTTPException(detail={
                "error": {
                    "message": f"Error. No user with the identifier {id} was found.",
                    "type": "UserError",
                    "code": 404
                }
            }, status_code=status.HTTP_404_NOT_FOUND)
