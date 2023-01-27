from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import List
from database import get_db
from models import BPlan, User
from domain.bplan import bplan_crud, bplan_schema
from domain.user.user_router import get_current_user

router = APIRouter(
    prefix="/bplan"
)


@router.post("/")
def bplan_create(
        _bplan_create: bplan_schema.BPlanCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    #
    bplan_crud.create_bplan(
        db, _bplan_create, current_user
    )


@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
def bplan_update(_bplan_update: bplan_schema.BPlanUpdate,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
    bplan_crud.update_bplan(
        db=db,
        bplan_update=_bplan_update,
        user=current_user
    )


@router.post("/update", status_code=status.HTTP_204_NO_CONTENT)
def bplan_update_newversion(_bplan_update: bplan_schema.BPlanUpdate,
                            db: Session = Depends(get_db),
                            current_user: User = Depends(get_current_user)):
    bplan_crud.update_bplan_newversion(
        db=db,
        user=current_user,
        bplan_update=_bplan_update
    )


@router.get("/list", response_model=bplan_schema.BPlanList)
def bplan_list(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    #
    bplan_list = bplan_crud.get_bplan_list_user(
        db, current_user
    )

    return {'BPlans': bplan_list}


@router.get("/{title}", response_model=bplan_schema.BPlanRead)
def bplan_read(title: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return bplan_crud.get_bplan_by_title(
        db,
        user=current_user,
        title=title
    )


@router.delete("/{title}", status_code=status.HTTP_204_NO_CONTENT)
def bplan_delete(title: str,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
    bplan_crud.delete_bplan_by_title(
        db=db,
        title=title,
        user=current_user
    )

