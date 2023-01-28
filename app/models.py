from sqlalchemy import Column, Integer, String,\
    Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


class BPlan(Base):
    __tablename__ = "bplan"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    version = Column(Integer, nullable=False)

    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="bplan_users")


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="portfolio_users")


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    img = Column(String, nullable=True)
    category = Column(String, nullable=False)

    num_views = Column(Integer, nullable=False)
    num_likes = Column(Integer, nullable=False)
    num_comments = Column(Integer, nullable=False)

    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    username = Column(String, ForeignKey("user.username"), nullable=False)
    user = relationship("User", backref="article_users")


class Comment(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)

    likes = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="article_users")

    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=False)

    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)
    article = relationship("Article", backref="comments")
