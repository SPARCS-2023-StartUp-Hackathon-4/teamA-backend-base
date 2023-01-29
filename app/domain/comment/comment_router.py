from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.comment import comment_schema, comment_schema
from domain.article import article_crud

router = APIRouter(
    prefix="/comment",
)


@router.post("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(article_id: int,
                  _comment_create: comment_schema.CommentCreate,
                  db: Session = Depends(get_db)):

    article = article_crud.get_article(article_id, db)
    if not article:
        raise HTTPException(status_code=404, detail="article not found")


