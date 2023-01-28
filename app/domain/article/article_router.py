from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import List
from database import get_db
from models import Article, User
from domain.article import article_schema, article_crud
from domain.user.user_router import get_current_user

router = APIRouter(
    prefix="/article"
)


@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def create_article(_create_article: article_schema.ArticleCreate,
                   db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    article_crud.create_article(_create_article=_create_article,
                                db=db, user=user)


@router.get("/{id}", response_model=article_schema.ArticleRead)
def read_article(id: int, db: Session = Depends(get_db)):
    return article_crud.read_article(id, db)


@router.get("/list", response_model=List[article_schema.ArticleRead])
def read_article_list(db: Session = Depends(get_db)):
    return article_crud.read_article_list(db)


@router.put("{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_article(id: int, _update_article: article_schema.ArticleCreate,
                   db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    article = read_article(id)
    if user.id == article.user_id:
        article_crud.update_article(_update_article=_update_article,
                                    article=article,
                                    db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id: int, db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    article = read_article(id)
    if user.id == article.user_id:
        article_crud.delete_article(article, db)
