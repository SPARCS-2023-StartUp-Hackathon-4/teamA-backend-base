from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.user import user_router
from domain.bplan import bplan_router
from domain.trend import trend_router
from domain.portfolio import portfolio_router


app = FastAPI()


origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router.router)
app.include_router(bplan_router.router)
app.include_router(trend_router.router)
app.include_router(portfolio_router.router)
