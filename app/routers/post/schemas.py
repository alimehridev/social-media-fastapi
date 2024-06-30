from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.routers.user.schemas import UserToResponse
from app.routers.vote.schemas import VoteToResponse

class PostSchema(BaseModel):
    title: str                      # title is a necessary item
    content: str                    # content is a necessary item
    published: bool = True          # published default value is true

class PostCreate(PostSchema):
    pass

class PostToResponse(PostSchema):
    id: int
    created_at: datetime
    owner: UserToResponse
    votes: List[VoteToResponse]

class PostToResponseWithVotes(BaseModel):
    Post: PostToResponse
    votes_count: int = 0