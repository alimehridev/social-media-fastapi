from app.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"

    id = Column("id", Integer, primary_key=True, nullable=False)
    title = Column("title", String(68), nullable=False)
    content  = Column("content", Text, nullable=False)
    published = Column("published", Boolean, nullable=False, server_default="TRUE")
    owner_id = Column("owner_id", ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    created_at = Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    
    owner = relationship("app.models.User")
