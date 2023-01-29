import datetime

from pydantic import BaseModel, validator
from typing import List


class CommentCreate(BaseModel):
    content: str


