from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str                      # title is a necessary item
    content: str                    # content is a necessary item
    published: bool = True          # published default value is true
