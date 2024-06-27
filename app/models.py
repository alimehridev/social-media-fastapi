from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from app.routers.post.models import Post
from app.routers.user.models import User
from app.routers.vote.models import Vote

class Post(Post):
    pass

class User(User):
    pass
    


class Vote(Vote):
    pass