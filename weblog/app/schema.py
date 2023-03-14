from __future__ import annotations
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional,BinaryIO


class UserSchema(BaseModel):
    email: EmailStr
    password: str = Field(unique=True, min_length=8)

    class Config:
        orm_mode = True


class CreateUserSchema(UserSchema):
    name: str = Field(unique=True)

    class Config:
        orm_mode = True


class UserSchemaOut(BaseModel):
    id: int
    role: str = "User"
    name: str = Field(unique=True)
    email: EmailStr
    posts: list[None | PostSchemaOut]

    class Config:
        orm_mode = True


class PostSchema(BaseModel):
    title: str
    # image: bytes
    content: str
    owner: UserSchemaOut

    class Config:
        orm_mode = True


class PostSchemaOut(PostSchema):
    comments: list[None | CommentSchemaOut]

    class Config:
        orm_mode = True


class CommentSchema(BaseModel):
    post: PostSchemaOut
    owner: UserSchemaOut
    text: str

    class Config:
        orm_mode = True


class CommentSchemaIn(BaseModel):
    post_id: int = Field(unique=True)
    comment_text: str

    class Config:
        orm_mode = True


class CommentSchemaOut(BaseModel):
    post_id: int = Field(unique=True)
    user_id: int = Field(unique=True)
    comment_date: str
    comment_text: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str]
    username: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

