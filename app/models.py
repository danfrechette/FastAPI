from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", name='posts_users_fkey', ondelete="CASCADE"), nullable=False) 
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at  = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User")
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False )
    created_at  = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String, nullable=True)

class Vote(Base):
     __tablename__ = "votes"
     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),primary_key=True, nullable=False)
     post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'),primary_key=True, nullable=False)
     
