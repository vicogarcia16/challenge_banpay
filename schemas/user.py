from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    films = "films"
    people = "people"
    locations = "locations"
    species = "species"
    vehicles = "vehicles"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: RoleEnum
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "user1",
                "email": "user1@example.com",
                "password": "password123",
                "role": "films"
            }
        }    
    }
    
class UserDisplay(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    role: RoleEnum
    model_config = ConfigDict(from_attributes=True)
    
class UserAuth(BaseModel):
    id: int
    username: str
    password: str