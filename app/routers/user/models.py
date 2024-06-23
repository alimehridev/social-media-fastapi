from app.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, nullable=False)
    email = Column("email", String(48), nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    created_at = Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))