from fastapi import FastAPI
from database import Base, engine
from routes.auth import router as auth_router
from routes.vpn import router as vpn_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(vpn_router)
