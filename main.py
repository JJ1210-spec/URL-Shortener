from database import engine,Base
from fastapi import FastAPI
from routers import router

app = FastAPI()
Base.metadata.create_all(bind = engine)

app.include_router(router)
