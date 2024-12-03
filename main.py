from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, ghibli, auth
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
load_dotenv() 

app = FastAPI(
    title="Challenge Banpay",
    description="Una REST API para el challenge de Banpay",
    version="1.0.0",
    docs_url="/",
    redoc_url="/redoc"
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(ghibli.router)

origins = os.getenv("ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)