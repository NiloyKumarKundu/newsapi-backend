import requests
from requests.exceptions import ReadTimeout, ConnectTimeout
from fastapi import File
from passlib.context import CryptContext
from tortoise.exceptions import IntegrityError
from tortoise.expressions import Q
from functools import reduce
from operator import or_
from models import User
from conf.response import CustomJSONResponse
from utils.token import create_access_token
from .pydantic_models import UserPydantic, Login


async def create_user_view(payload: UserPydantic):
    payload.password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash(payload.password)
    try:
        user = await User.create(**payload.model_dump(exclude=["id", "created_at", "updated_at"]))
    except IntegrityError:
        return CustomJSONResponse(content=None, message="User already exists", status_code=400)
    access_token = create_access_token(user_id=user.id)
    return CustomJSONResponse(content={"data": {"id": user.id, "username": user.username, "token": access_token}}, status_code=201)


async def login_user_view(payload: Login):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    username_conditions = [Q(username=payload.username), Q(email=payload.username)]
    username_q = reduce(or_, username_conditions)
    user = await User.filter(username_q).first()
    if not user or not password_context.verify(payload.password, user.password):
        return CustomJSONResponse(content=None, message="Invalid credentials", status_code=400)
    access_token = create_access_token(user_id=user.id)
    return CustomJSONResponse(content={"data": {"id": user.id, "username": user.username, "token": access_token}}, status_code=200)
