from pydantic import BaseModel

class Post(BaseModel):
    title: str                      # title is a necessary item
    content: str                    # content is a necessary item
    published: bool = True          # published default value is true
