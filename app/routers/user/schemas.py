from pydantic import BaseModel, EmailStr
from datetime import datetime

# User Schemas
class UserSchema(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserSchema):
    pass

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
