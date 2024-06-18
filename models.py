from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str                      # title is a necessary item
    content: str                    # content is a necessary item
    published: bool = 1             # published default value is 1
    rating: Optional[float] = None    # rating is optional and its default value is None
