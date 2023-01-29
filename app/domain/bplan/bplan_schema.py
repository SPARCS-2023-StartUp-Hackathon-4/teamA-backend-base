import datetime

from pydantic import BaseModel, validator
from typing import List


class BPlanBase(BaseModel):
    title: str
    content: str
    version: int
    create_date: datetime.datetime
    update_date: datetime.datetime

    class Config:
        orm_mode = True


class BPlanRead(BaseModel):
    title: str
    content: str
    version: int

    class Config:
        orm_mode = True


class BPlanUpdate(BaseModel):
    title: str
    content: str
    version: int

    class Config:
        orm_mode = True


class BPlanCreate(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class BPlanList(BaseModel):
    BPlans: List[BPlanRead]

    class Config:
        orm_mode = True
