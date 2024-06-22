from .database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"

    id = Column("id", Integer, primary_key=True, nullable=False)
    title = Column("title", String(68), nullable=False)
    content  = Column("content", Text, nullable=False)
    published = Column("published", Boolean, nullable=False, server_default="TRUE")
    created_at = Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, nullable=False)
    email = Column("email", String(48), nullable=False, unique=True)
    password = Column("password", String(48), nullable=False)
    created_at = Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))