from abc import ABC, abstractmethod
from typing import Union, Tuple
from fastapi import HTTPException, Request
from tortoise.exceptions import DoesNotExist
from models import User


class BasePermission(ABC):
    async def __call__(self, request: Request):
        has_permission = await self.has_permission(request)
        if isinstance(has_permission, bool) and not has_permission:
            raise HTTPException(detail='You do not have permission to perform this action', status_code=403)
        if isinstance(has_permission, tuple) and not has_permission[0]:
            raise HTTPException(detail=f'{has_permission[1]}', status_code=403)
        return None

    @abstractmethod
    async def has_permission(self, request: Request) -> Union[bool, Tuple[bool, str]]:
        pass


class IsAuthenticated(BasePermission):
    """Permission Class For Authencated Users"""

    async def has_permission(self, request: Request) -> bool | Tuple[bool | str]:
        if not request.state.is_authenticated:
            raise HTTPException(detail='Authentication Failed! Invalid Credentials!', status_code=401)
        try:
            user = await User.get(id=request.state.user_id)
            if user.deleted_at:
                raise HTTPException(detail='Authentication Failed! Invalid Credentials!', status_code=401)
            return True
        except DoesNotExist:
            raise HTTPException(detail='Authentication Failed! Invalid Credentials!', status_code=401)

