from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db import models
from db.database import engine
from routers import user, ghibli, auth
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from tools.exceptions import (
    UserNotFoundError, 
    InvalidCredentialsError, 
    TokenExpiredError,
    NoUsersFoundError,
    UsernameTakenError,
    EmailTakenError
)

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

@app.exception_handler(UserNotFoundError)
async def user_not_found_exception_handler(request: Request, 
                                           exc: UserNotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(InvalidCredentialsError)
async def invalid_credentials_exception_handler(request: Request, 
                                                exc: InvalidCredentialsError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(TokenExpiredError)
async def token_expired_exception_handler(request: Request, 
                                          exc: TokenExpiredError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(NoUsersFoundError)
async def no_users_found_exception_handler(request: Request, 
                                           exc: NoUsersFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(UsernameTakenError)
async def username_taken_exception_handler(request: Request, 
                                           exc: UsernameTakenError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(EmailTakenError)
async def email_taken_exception_handler(request: Request, 
                                        exc: EmailTakenError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )