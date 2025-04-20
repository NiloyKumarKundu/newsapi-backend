import datetime
import requests
from requests.exceptions import ReadTimeout, ConnectTimeout
from fastapi import File
from passlib.context import CryptContext
from tortoise.exceptions import IntegrityError
from tortoise.expressions import Q
from functools import reduce
from operator import or_
from models import User, News
from conf.response import CustomJSONResponse
from fastapi import APIRouter, Request
from conf.global_vars import NEWS_API_ENDPOINT, NEWS_API_KEY



async def get_all_news_views(request: Request, q: str, language: str, sort_by: str, page_size: int):
    try:
        params = {
            "q": q,
            "language": language,
            "sortBy": sort_by,
            "pageSize": page_size
        }

        headers = {
            "Authorization": f"Bearer {NEWS_API_KEY}"
        }

        response = requests.get(NEWS_API_ENDPOINT, headers=headers, params=params)

        if response.status_code == 200:
            return CustomJSONResponse(status_code=200, content=response.json())
        else:
            return CustomJSONResponse(
                status_code=response.status_code,
                content={"message": "Failed to fetch news", "details": response.text}
            )
    except requests.exceptions.RequestException as e:
        return CustomJSONResponse(status_code=500, content={"message": "Request failed", "error": str(e)})
    
    



async def save_latest_news_view(request: Request):
    try:
        params = {
            "q": "news",
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 3,
        }
        print(f"news api key: {NEWS_API_KEY}")

        headers = {
            "Authorization": f"Bearer {NEWS_API_KEY}"
        }

        response = requests.get(NEWS_API_ENDPOINT, headers=headers, params=params)

        if response.status_code != 200:
            return CustomJSONResponse(
                status_code=response.status_code,
                content={"message": "Failed to fetch news", "details": response.text}
            )

        news_data = response.json().get("articles", [])[:3]
        
        saved_news = []

        for article in news_data:
            try:
                await News.create(
                    title=article['title'],
                    desc=article["description"],
                    url=article["url"],
                    published_at=article["publishedAt"]
                )
                saved_news.append(article['title'])
            except Exception as e:
                raise e

        return CustomJSONResponse(
            status_code=201,
            content={"message": f"{len(saved_news)} news articles saved", "titles": saved_news}
        )

    except requests.exceptions.RequestException as e:
        return CustomJSONResponse(status_code=500, content={"message": "Request failed", "error": str(e)})
