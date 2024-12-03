from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=403, 
                    detail="Forma de autenticación inválida. Se requiere 'Bearer'."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, 
                    detail="Token inválido o ha expirado."
                )
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, 
                detail="Código de autorización inválido o ausente."
            )

    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            payload = decodeJWT(jwtoken)
            return payload is not None
        except Exception as e:
            return False
