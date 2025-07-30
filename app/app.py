from fastapi import FastAPI
from app.presentation import routers

app = FastAPI()

# router 등록
for router in routers:
    app.include_router(router)
