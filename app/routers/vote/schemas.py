from pydantic import BaseModel
from app.routers.user.schemas import UserToResponse

class Vote(BaseModel):
    post_id: int

class VoteToResponse(Vote):
    user: UserToResponse