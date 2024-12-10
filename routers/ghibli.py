from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_ghibli import get_ghibli_data
from db.db_user import get_user_by_username
from schemas.user import RoleEnum

router = APIRouter(
    prefix="/ghibli",
    tags=["ghibli"],
    responses={404: {"description": "No encontrado"}}
)

@router.get("/{username}/")
def get_ghibli_data_by_username(username: str, db: Session = Depends(get_db)):
    """
    Obtiene los datos de Studio Ghibli según el rol del usuario.

    - **username**: Nombre de usuario utilizado para identificar al usuario en la base de datos.
    - Si el rol del usuario no es 'admin', se obtienen los datos específicos del rol (films, people, locations, species, vehicles).
    - Si el rol del usuario es 'admin', se obtienen los datos de todos los roles combinados.
    """
    user = get_user_by_username(db, username)
    user_role = RoleEnum(user.role)
    datos = get_ghibli_data(user_role)
    return datos
