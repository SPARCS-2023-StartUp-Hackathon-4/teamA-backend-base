import datetime

from pydantic import BaseModel, validator
from typing import List


class PortfolioCreate(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True
