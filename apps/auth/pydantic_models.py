from pydantic import BaseModel, model_validator, field_validator
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from enum import Enum

from models import User
from utils.pattern_validators import is_valid_email, is_possible_phone_number, is_valid_url


UserBasePydantic = pydantic_model_creator(User, name="User", include=(
    "id", "first_name", "last_name", "email", "username", "password", "created_at", "updated_at"))

UserResponse = pydantic_model_creator(User, name="UserResponse", include=(
    "id", "first_name", "last_name", "email", "username", "created_at", "updated_at"))


class UserPydantic(UserBasePydantic):
    id: Optional[None] = None
    email: str
    password: str
    first_name: str
    created_at: Optional[None] = None
    updated_at: Optional[None] = None



class Login(BaseModel):
    username: str
    password: str
