from sqlalchemy import Column, DateTime, Boolean, func, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes

from db_connection import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    first_name = Column(sqltypes.String(30), nullable=False)
    last_name = Column(sqltypes.String(30), nullable=False)
    telegram_user_id = Column(sqltypes.String(30), unique=True)
    last_active = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)


'''class Session(BaseModel):
    __tablename__ = "sessions"

    user_id = Column(sqltypes.Integer, ForeignKey("users.id"), nullable=False)
    end_time = Column(DateTime(timezone=True), server_default=func.now())'''


class Message(BaseModel):
    __tablename__ = "messages"

    user_id = Column(sqltypes.Integer, ForeignKey("users.id"))
    prompt = Column(sqltypes.Text)
    reply = Column(sqltypes.Text)

    # user = relationship("User", back_populates="users")



