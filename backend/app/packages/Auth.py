from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

from fastapi import HTTPException, Header, Depends, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse

from sqlmodel import Session
from app.configurations.database import engine

from app.models import (
    User,
    UserType
)

from app.configurations.enviroments import (
    ENCRYPTION_ALGORITHM,
    SECRET_KEY,
    ACCESS_TOKEN_EXPIRES,
    REFRESH_TOKEN_EXPIRES
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_token(user: User, type: str) -> str:
    allowed_types = ["refresh", "access"]

    if type not in allowed_types:
        raise ValueError("Invalid token type")

    data = {
        "id": user.id,
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "created_at": f"{user.created_at}",
        "updated_at": f"{user.updated_at}",
    }

    match type:
        case "refresh":
            data["exp"] = datetime.utcnow(
            ) + timedelta(hours=REFRESH_TOKEN_EXPIRES)
        case "access":
            data["exp"] = datetime.utcnow(
            ) + timedelta(minutes=ACCESS_TOKEN_EXPIRES)

    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ENCRYPTION_ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[
                             ENCRYPTION_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def decode_header_token(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[
                                 ENCRYPTION_ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def is_token_valid(expiration_date: str) -> bool:
    current_time = datetime.utcnow()
    return current_time < expiration_date


def get_user_by_id(user_id: int) -> User:
    with Session(engine) as session:
        user_exists = session.query(User).filter(
            User.id == user_id).first()

        if not user_exists:
            raise HTTPException(
                detail={
                    "error": {
                        "message": "User does not exist",
                        "type": "UserError",
                        "code": 404
                    }
                },
                status_code=404
            )

        return user_exists


def get_current_user(authorization: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = decode_header_token(authorization)
        user_id = payload.get("id")

        user = get_user_by_id(user_id)

        return user
    except HTTPException as e:
        raise e

def is_user_administrator(user: User = Depends(get_current_user)):
    if user.type != UserType.administrator:
        raise HTTPException(
            detail={
                "error": {
                    "message": "Error. You don't have permission to perform this operation. You need to be an administrator.",
                    "type": "UserError",
                    "code": 403
                }
            },
            status_code=status.HTTP_403_FORBIDDEN
        )
    return user
