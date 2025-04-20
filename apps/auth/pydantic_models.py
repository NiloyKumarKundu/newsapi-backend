from pydantic import BaseModel
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from models import User


UserBasePydantic = pydantic_model_creator(User, name="User", include=(
    "id", "first_name", "last_name", "email", "username", "password", "created_at", "updated_at"))

class UserPydantic(UserBasePydantic):
    id: Optional[None] = None
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    created_at: Optional[None] = None
    updated_at: Optional[None] = None



class Login(BaseModel):
    username: str
    password: str
