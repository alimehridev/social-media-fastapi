from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text


class Vote(Base):
    __tablename__ = "votes"

    post_id = Column("post_id", ForeignKey("posts.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, primary_key=True)
    user_id = Column("user_id", ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, primary_key=True)
    created_at = Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    post = relationship("app.models.Post")
    user = relationship("app.models.User")