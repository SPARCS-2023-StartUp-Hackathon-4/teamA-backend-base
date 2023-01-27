from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import List
from database import get_db
from models import Portfolio, User
from domain.portfolio import portfolio_schema, portfolio_crud
from domain.user.user_router import get_current_user

router = APIRouter(
    prefix="/portfolio"
)


@router.get("/list", response_model=list[portfolio_schema.PortfolioCreate])
def read_portfolio_list(db: Session = Depends(get_db),
                        user: User = Depends(get_current_user)):
    _portfolio = portfolio_crud.read_portfolio_list(db=db, user=user)
    return _portfolio


@router.get("/{title}", response_model=portfolio_schema.PortfolioCreate)
def read_portfolio(title: str,
                   db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    _portfolio = portfolio_crud.read_portfolio(db, title, user)
    # TODO: Exception
    return _portfolio


@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def create_portfolio(_portfolio_create: portfolio_crud.PortfolioCreate,
                     db: Session = Depends(get_db),
                     user: User = Depends(get_current_user)):
    portfolio_crud.create_portfolio(db,
                                    _portfolio_create,
                                    user)
    return True


@router.delete("/{title}")
def delete_portfolio(title: str,
                     db: Session = Depends(get_db),
                     user: User = Depends(get_current_user)):
    done = portfolio_crud.delete_portfolio(db, title, user)
    if not done:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail='Not existing portfolio',
        )


@router.put("/")
def update_portfolio(_update_portfolio: portfolio_crud.PortfolioCreate,
                     db: Session = Depends(get_db),
                     user: User = Depends(get_current_user)):
    done = portfolio_crud.update_portfolio(db=db, portfolio_update=_update_portfolio, user=user)

    if not done:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail='Not existing portfolio',
        )
