from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostSchema(BaseModel):
    title: str                      # title is a necessary item
    content: str                    # content is a necessary item
    published: bool = True          # published default value is true

class PostCreate(PostSchema):
    pass

class PostResponse(PostSchema):
    id: int
    created_at: datetime