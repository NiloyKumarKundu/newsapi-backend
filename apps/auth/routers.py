from fastapi import APIRouter, Request, Depends
from conf.permissions import IsAuthenticated
from .pydantic_models import UserPydantic, Login
from .view import create_user_view, login_user_view



router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)


@router.post("/signup")
async def create_user(request: Request, payload: UserPydantic):
    return await create_user_view(payload)


@router.post("/login")
async def login_user(request: Request, payload: Login):
    return await login_user_view(payload)