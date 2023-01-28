from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.user import user_router
from domain.bplan import bplan_router
# from domain.vac import vac_router
from domain.portfolio import portfolio_router


app = FastAPI()


app.include_router(user_router.router)
app.include_router(bplan_router.router)
# app.include_router(vac_router.router)
app.include_router(portfolio_router.router)
