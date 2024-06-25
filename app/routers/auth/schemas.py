from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Auth Schemas
class UserSchema(BaseModel):
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

class Token(BaseModel):
    token: str
    token_type: str