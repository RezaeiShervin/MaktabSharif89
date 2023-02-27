from pydantic import BaseModel, constr, EmailStr
from datetime import datetime

password_regex = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"

class User(BaseModel):
    username: constr(min_length=8, max_length=100)
    email: EmailStr
    created_at: datetime = datetime.now()

class UserUpdate(User):
    username: constr(min_length=7, max_length=100) = None
    email: EmailStr = None
    created_at: datetime = datetime.now()

class UserBase(User):
    password: constr(min_length=7, max_length=100, regex=password_regex)

