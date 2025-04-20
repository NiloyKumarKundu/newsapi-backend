from typing import Optional
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from models import News

NewsBasePydantic = pydantic_model_creator(
    News,
    name="News",
    include=("id", "title", "desc", "url", "published_at", "updated_at", "user_id")
)

class NewsCustomSchema(BaseModel):
    id: Optional[int] = None
    title: str
    desc: str
    url: str
    published_at: Optional[str] = None
    updated_at: Optional[str] = None
    user_id: Optional[int] = None

    class Config:
        orm_mode = True
