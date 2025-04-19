from fastapi import APIRouter, Request, Depends, File, UploadFile
from conf.permissions import IsAuthenticated



router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}}
)
