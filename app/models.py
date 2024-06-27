from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from app.routers.post.models import Post
from app.routers.user.models import User

class Post(Post):
    pass

class User(User):
    pass
    


class Vote(Base):
    __tablename__ = "votes"

    id = Column("id", Integer, primary_key=True, nullable=False)
    post_id = Column("post_id", ForeignKey("posts.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    user_id = Column("user_id", ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    created_at = Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    post = relationship("app.models.Post")
    user = relationship("app.models.User")