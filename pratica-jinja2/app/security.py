from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.testing import db

from . import models
from .config import settings

oauth2 = OAuth2PasswordBearer(tokenUrl="admin/login")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt

async def get_current_customer(token: str = Depends(oauth2)):
    return await verify_token(token, models.Admin)


async def verify_token(token: str, model):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")

        customer = db.query(model).filter(model.email == email).first()
        if not customer:
            raise HTTPException(status_code=401, detail="User not found")

        return customer
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
