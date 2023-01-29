from datetime import datetime

from sqlalchemy.orm import Session

from domain.portfolio.portfolio_schema import PortfolioCreate
from models import Portfolio, User


def create_portfolio(db: Session,
                     portfolio_create: PortfolioCreate,
                     user: User):
    db_portfolio = Portfolio(
        title=portfolio_create.title,
        content=portfolio_create.content,
        create_date=datetime.now(),
        update_date=datetime.now(),
        user=user
    )
    db.add(db_portfolio)
    db.commit()


def read_portfolio(db: Session,
                   title: str,
                   user: User):
    db_portfolio = db.query(Portfolio).filter((Portfolio.user_id == user.id) & (Portfolio.title == title)).first()
    return db_portfolio


def read_portfolio_list(db: Session,
                        user: User):
    db_portfolio = db.query(Portfolio).filter((Portfolio.user_id == user.id)).all()
    return db_portfolio


def update_portfolio(db: Session,
                     portfolio_update: PortfolioCreate,
                     user: User):
    db_portfolio = db.query(Portfolio).filter((portfolio_update.title == Portfolio.title) &
                                              (user.id == Portfolio.user_id)).first()

    if not db_portfolio:
        return False

    db_portfolio.title = portfolio_update.title
    db_portfolio.content = portfolio_update.content
    db_portfolio.update_date = datetime.now()
    db.add(db_portfolio)
    db.commit()

    return True


def delete_portfolio(db: Session,
                     title: str,
                     user: User):
    db_portfolio = db.query(Portfolio).filter((Portfolio.user_id == user.id) &
                               (Portfolio.title == title)).first()

    if not db_portfolio:
        return False

    db.delete(
        db_portfolio
    )
    db.commit()

    return True
