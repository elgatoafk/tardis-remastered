from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.util.db import Base


class TimeZone(Base):
    """Class representing timezones used in the app."""
    __tablename__ = 'timezones'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    is_default = Column(Boolean, default=False)


class InviteCode(Base):
    """Table storing invite codes to register at admin dashboard"""
    __tablename__ = 'invite_codes'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    is_used = Column(Boolean, default=False)
    created_by = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="invite_codes")


class User(Base):
    """Table storing user information."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_owner = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=True)
    invite_codes = relationship("InviteCode", back_populates="owner")
