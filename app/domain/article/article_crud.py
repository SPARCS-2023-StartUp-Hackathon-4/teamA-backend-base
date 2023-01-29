from datetime import datetime

from sqlalchemy.orm import Session

from domain.article import article_schema, article_router
from models import Article, User


def create_article(_create_article: article_schema.ArticleCreate,
                   db: Session,
                   user: User):
    db_article = Article(
        title=_create_article.title,
        content=_create_article.content,
        tags=_create_article.tags,
        img=_create_article.img,
        category=_create_article.category,

        num_views=0,
        num_likes=0,
        num_comments=0,

        create_date=datetime.now(),
        update_date=datetime.now(),

        user=user
    )
    db.add(db_article)
    db.commit()


def read_article(id: int, db: Session):
    return db.query(Article).get(id)


def read_article_list(db: Session):
    return db.query(Article).all()


def update_article(_update_article: article_schema.ArticleCreate,
                        article: Article, db: Session):
    article.title = _update_article.title
    article.content = _update_article.content
    article.tags = _update_article.tags
    article.img = _update_article.img
    article.category = _update_article.category

    article.update_date = datetime.now()

    db.add(article)
    db.commit()


def delete_article(article: Article, db: Session):
    db.delete(article)

