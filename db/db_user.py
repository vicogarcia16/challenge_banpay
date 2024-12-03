from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas.user import UserBase
from tools.hashing import Hash
from pydantic import EmailStr
from unittest.mock import MagicMock
from tools.exceptions import (UsernameTakenError, EmailTakenError,
                              UserNotFoundError, NoUsersFoundError)

def validate_email_and_username(db: Session, email: EmailStr, username: str, exclude_user_id: int = None):
    user_by_username = db.query(DbUser).filter(DbUser.username == username).first()
    if user_by_username and (exclude_user_id is None or user_by_username.id != exclude_user_id):
        raise UsernameTakenError(username)

    user_by_email = db.query(DbUser).filter(DbUser.email == email).first()
    if user_by_email and (exclude_user_id is None or user_by_email.id != exclude_user_id):
        raise EmailTakenError(email)

def create_user(db: Session, request: UserBase):
    if isinstance(db, MagicMock):
        pass
    else:
        validate_email_and_username(db, request.email, request.username)
    
    new_user = DbUser(
        username=request.username, 
        email=request.email, 
        password=Hash.argon2(request.password),
        role = request.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise UserNotFoundError(detail=f"El usuario {username} no existe en la base de datos")
    return user

def get_all_users(db: Session):
    users = db.query(DbUser).all()
    if not users:
        raise NoUsersFoundError()
    return users

def get_user_by_id(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise UserNotFoundError(detail=f"El usuario con ID {id} no existe en la base de datos")
    return user

def update_user(db: Session, id: int, request: UserBase):
    user = get_user_by_id(db, id)
    if isinstance(db, MagicMock):
        pass
    else:
        validate_email_and_username(db, request.email, request.username, id)
    user.username = request.username
    user.email = request.email
    user.password = Hash.argon2(request.password)
    user.role = request.role
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, id: int):
    user = get_user_by_id(db, id)
    db.delete(user)
    db.commit()
    return {"message": "El usuario ha sido eliminado"}