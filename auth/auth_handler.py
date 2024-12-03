import time
from typing import Dict
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRY = 600
REFRESH_TOKEN_EXPIRY = 60 * 60 * 24 * 7

def token_response(access_token: str, refresh_token: str,
                   access_expires: float, refresh_expires: float) -> Dict[str, str]:
    current_time = time.time()
    access_seconds_left = access_expires - current_time
    refresh_seconds_left = refresh_expires - current_time
    
    access_expires_in_minutes = max(0, access_seconds_left / 60)  
    refresh_expires_in_days = max(0, refresh_seconds_left / (60 * 60 * 24))
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "access_expires_in": f"{access_expires_in_minutes:.2f} minutos",
        "refresh_expires_in": f"{refresh_expires_in_days:.2f} días"
    }

def signJWT(username: str) -> Dict[str, str]:
    access_expires = time.time() + ACCESS_TOKEN_EXPIRY
    refresh_expires = time.time() + REFRESH_TOKEN_EXPIRY
    
    access_token_payload = {
        "username": username,
        "expires": access_expires
    }
    
    refresh_token_payload = {
        "username": username,
        "expires": refresh_expires
    }

    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm=ALGORITHM)

    return token_response(access_token, refresh_token, access_expires, refresh_expires)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if decoded_token["expires"] >= time.time():
            return decoded_token
        else:
            return {"error": "Token expirado"}
    except jwt.ExpiredSignatureError:
        return {"error": "Token expirado"}
    except jwt.InvalidTokenError:
        return {"error": "Token inválido"}
    except Exception as e:
        return {"error": str(e)}

def verify_refresh_token(refresh_token: str) -> dict:
    try:
        decoded_token = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        if decoded_token["expires"] >= time.time():
            return decoded_token
        return None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
