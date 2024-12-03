from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db import db_user
from db.database import get_db
from typing import List
from schemas.user import UserBase, UserDisplay
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"descripcion": "No encontrado"}}
    )

@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    """ Crea un nuevo usuario en la base de datos. """
    return db_user.create_user(db, request)

@router.get("/all/", response_model=List[UserDisplay])
def get_users(db: Session = Depends(get_db)):
    """ Obtiene todos los usuarios de la base de datos. """
    return db_user.get_all_users(db)

@router.get("/{id}/", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    """ Obtiene un usuario de la base de datos mediante su ID. """
    return db_user.get_user_by_id(db, id)

@router.put("/{id}/", response_model=UserDisplay, dependencies=[Depends(JWTBearer())])
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    """ Actualiza un usuario de la base de datos mediante su ID. """
    return db_user.update_user(db, id, request)

@router.delete("/{id}/", dependencies=[Depends(JWTBearer())])
def delete_user(id: int, db: Session = Depends(get_db)):
    """ Elimina un usuario de la base de datos mediante su ID. """
    return db_user.delete_user(db, id)
