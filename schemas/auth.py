from pydantic import BaseModel

class LoginBase(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "user1",
                "password": "password123"
            }
        }
    }
        
class RefreshToken(BaseModel):
    refresh_token: str