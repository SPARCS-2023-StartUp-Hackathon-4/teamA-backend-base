from datetime import datetime

from sqlalchemy.orm import Session

from domain.bplan.bplan_schema import BPlanCreate, BPlanUpdate
from models import BPlan, User


def create_bplan(db: Session, bplan_create: BPlanCreate, user: User):
    db_bplan = BPlan(
        title=bplan_create.title,
        content=bplan_create.content,
        create_date=datetime.now(),
        update_date=datetime.now(),
        version=1,
        user=user
    )
    db.add(db_bplan)
    db.commit()


def get_bplan_list_user(db: Session, user: User):
    return db.query(BPlan).filter(BPlan.user_id == user.id).all()


def get_bplan_by_title(db: Session, user: User, title: str):
    return db.query(BPlan).filter(
        (BPlan.user_id == user.id) & (BPlan.title == title)
    ).order_by(BPlan.version).first()


def delete_bplan_by_title(db: Session, user: User, title: str):
    db_bplan = db.query(BPlan).filter(
        (BPlan.user_id == user.id) & (BPlan.title == title)
    ).all()
    for bplan_single in db_bplan:
        db.delete(bplan_single)
    db.commit()


def update_bplan(db: Session, user: User, bplan_update: BPlanUpdate):
    db_bplan = db.query(BPlan).filter(
        (BPlan.user_id == user.id) & (BPlan.title == bplan_update.title)
    ).order_by(BPlan.version).first()

    db_bplan.title = bplan_update.title
    db_bplan.content = bplan_update.content
    db_bplan.update_date = datetime.now()

    db.commit()


def update_bplan_newversion(db: Session, user: User, bplan_update: BPlanUpdate):
    db_bplan_prev = db.query(BPlan).filter(
        (BPlan.user_id == user.id) & (BPlan.title == bplan_update.title)
    ).order_by(BPlan.version).first()

    db_bplan = BPlan(
        title=bplan_update.title,
        content=bplan_update.content,
        create_date=db_bplan_prev.create_date,
        update_date=datetime.now(),
        user=user,
        version=db_bplan_prev.version+1
    )

    db.add(db_bplan)

    db.commit()
