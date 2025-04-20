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
async def get_all_news(
    request: Request,
    q: str = Query(..., description="Search query"),
    language: str = Query("en", description="Language of the news"),
    sort_by: str = Query("publishedAt", alias="sortBy", description="Sort by"),
    page_size: int = Query(10, alias="pageSize", ge=1, le=100, description="Number of articles")
):
    return await get_all_news_views(request, q, language, sort_by, page_size)


@router.post("/save_latest_news")
async def save_latest_news(request: Request):
    return await save_latest_news_view(request)