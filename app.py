import os
import asyncio
import importlib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.middleware import Middleware
from tortoise.contrib.fastapi import register_tortoise
from pydantic import ValidationError
from contextlib import asynccontextmanager
from conf.middlewares import AuthenticationMiddleware
from conf.global_vars import APPS
from conf.database import TORTOISE_CONFIG


middleware = [
    Middleware(CORSMiddleware,
               allow_origins=["*"],
               allow_credentials=True,
               allow_methods=["*"],
               allow_headers=["*"]),
    Middleware(AuthenticationMiddleware)
]


async def not_found(request, exc):
    return PlainTextResponse(content='Page Not Found!', status_code=404)


exceptions = {
    404: not_found,
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Add Routers And Resolve Dependencies
    for module in APPS:
        mod = importlib.import_module(f'apps.{module}.routers')
        app.include_router(mod.router)
    yield

app = FastAPI(middleware=middleware, exception_handlers=exceptions, lifespan=lifespan)


register_tortoise(
    app=app,
    config=TORTOISE_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True,
)
