from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from collections import Counter
import pickle

router = APIRouter(
    prefix="/trend"
)


@router.get("/")
def get_trend():
    with open('counts.pickle', 'rb') as f:
        counts = pickle.load(f)
        counts: Counter
    return {
        'trend': sorted([(x, y) for x, y in dict(counts).items()], key=lambda x: x[1], reverse=True)
    }