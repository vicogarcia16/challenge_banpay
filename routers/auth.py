from fastapi import APIRouter, Depends, HTTPException
from db.db_user import get_user_by_username
from sqlalchemy.orm.session import Session
from db.database import get_db
from schemas.auth import LoginBase, RefreshToken
from auth.auth_handler import signJWT, verify_refresh_token

router = APIRouter(
    tags=['authentication']
)

@router.post('/login/')
def login(request: LoginBase, db: Session = Depends(get_db)):
    """
    Recibe un nombre de usuario y una contraseña y devuelve un token de acceso si el usuario existe en la base de datos.
    """
    user = get_user_by_username(db, request.username)
    return signJWT(user.username)
    

@router.post("/refresh/")
def refresh_token(request: RefreshToken):
    """
    Recibe un refresh token y devuelve un nuevo access token si el refresh token es válido.
    """
    payload = verify_refresh_token(request.refresh_token)
    if payload:
        new_access_token = signJWT(payload["username"])["access_token"]
        return {"access_token": new_access_token}
    else:
        raise HTTPException(status_code=401, detail="Refresh token inválido o expirado")
    
    