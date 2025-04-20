import datetime
import math
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



async def get_all_news_views(request: Request, page, limit):
    try:
        params = {
            "q": "news",
            "language": 'en',
            "sortBy": 'popularity',
            "pageSize": 100
        }

        headers = {
            "Authorization": f"Bearer {NEWS_API_KEY}"
        }

        response = requests.get(NEWS_API_ENDPOINT, headers=headers, params=params)

        if response.status_code != 200:
            return CustomJSONResponse(
                status_code=response.status_code,
                content={
                    "message": "Failed to fetch news",
                    "details": response.text
                }
            )

        all_articles = response.json().get("articles", [])
        total_items = len(all_articles)
        total_pages = math.ceil(total_items / limit) if total_items else 0

        # calculate slice
        start = (page - 1) * limit
        end = start + limit
        page_articles = all_articles[start:end] if start < total_items else []

        return CustomJSONResponse(
            status_code=200,
            content={
                "page": page,
                "limit": limit,
                "total_pages": total_pages,
                "total_items": total_items,
                "articles": page_articles
            }
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
