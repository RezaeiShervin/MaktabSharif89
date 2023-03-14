from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, TIMESTAMP,BLOB
from .DataBase.my_database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(20))
    name = Column(String(20), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(20))
    posts = relationship("Post", back_populates="users")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(ForeignKey(User.id))
    owner = relationship(User, back_populates="posts")
    title = Column(String(20))
    # image = Column(BLOB)
    content = Column(Text)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    comments = relationship("Comment", back_populates="posts")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(ForeignKey(Post.id))
    post = relationship("Post", back_populates="Pcomments")
    owner_id = Column(ForeignKey(User.id))
    owner = relationship("User", back_populates="Ucomments")
    created_at = Column(TIMESTAMP)
    text = Column(Text)




