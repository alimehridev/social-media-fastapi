from pydantic import BaseModel

class PostSchema(BaseModel):
    title: str                      # title is a necessary item
    content: str                    # content is a necessary item
    published: bool = True          # published default value is true

class PostCreate(PostSchema):
    pass