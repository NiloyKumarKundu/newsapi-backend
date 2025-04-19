import jwt
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from conf.global_vars import JWT_SECRET


class HTTPRemoteDisconnectedMixin:
    async def __call__(self, scope, receive, send) -> None:
        if scope['type'] == 'http':
            request = Request(scope, receive, send)
            try:
                await super().__call__(scope, receive, send)
            except RuntimeError as e:
                if not await request.is_disconnected():
                    raise e
        else:
            await super().__call__(scope, receive, send)


class AuthenticationMiddleware(HTTPRemoteDisconnectedMixin, BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        request.state.headers = dict(request.headers)
        request.state.server = {}
        authorization = request.headers.get('authorization')
        request.state.is_authenticated = False
        if authorization:
            token = authorization.split(" ")[-1]
            try:
                payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
                request.state.user_id = payload.get('user_id', 0)
                request.state.is_authenticated = True
            except Exception as error:
                raise error

        response = await call_next(request)
        return response
