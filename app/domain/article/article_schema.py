import datetime

from pydantic import BaseModel, validator
from typing import List


class ArticleBase(BaseModel):
    pass



class ArticleRead(BaseModel):
    id: int
    title: str
    content: str
    tags: str
    img: str | None = None
    category: str

    num_views: int = 0
    num_likes: int = 0
    num_comments: int = 0

    username: str
    user_id: int

    class Config:
        orm_mode = True


class ArticleCreate(BaseModel):
    title: str
    content: str
    tags: str
    img: str | None = None
    category: str

    class Config:
        orm_mode = True
