from fastapi import APIRouter, Query, Request, Depends
from conf.permissions import IsAuthenticated
from .view import get_all_news_views, save_latest_news_view



router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(IsAuthenticated)]
)


@router.get("/")
async def get_all_news(request: Request, page: int = Query(1, gt=0), limit: int = Query(10, gt=0, le=100)):
    return await get_all_news_views(request, page, limit)


@router.post("/save-latest")
async def save_latest_news(request: Request):
    return await save_latest_news_view(request)