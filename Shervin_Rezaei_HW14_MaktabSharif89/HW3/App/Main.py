from pathlib import Path
from fastapi import Depends, FastAPI, APIRouter, HTTPException, Request, Response, status
from fastapi.params import Body
from typing import List, Dict
from sqlalchemy.orm import Session
from .DataBase import get_db
from . import Models
from fastapi.templating import Jinja2Templates
from Schemas.Users import UserBase, UserUpdate


app = FastAPI()
api_router = APIRouter()
BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@api_router.get("/", status_code=200)
def root():
    return {'message: Hi'}


@api_router.get("/users")
async def get_users(request: Request , db: Session = Depends(get_db)):
    users = db.query(Models.User).all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@api_router.get("/users/{id}")
def get_user(id : int, response : Response, db : Session = Depends(get_db)) -> dict:
    user = db.query(Models.User).filter(Models.User.id == id).first()
    return {"data" : user}


@api_router.post("/users", status_code=201)
async def register_user(new_user: UserBase, db: Session = Depends(get_db)):
    user = Models.User(**new_user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'data': user}

@api_router.delete("/users/{id}")
def delete_user(id: int, db: Session=Depends(get_db)):
    user = db.query(Models.User).filter(Models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user with id {id} does not exit"
        )
    user.delete(synchronize_session=False)
    db.commit()
    return {"data":"user deleted"}

@api_router.put("/users/{id}")
def update_user(id:int, updated_user:UserUpdate, db: Session=Depends(get_db)):
    user = db.query(Models.User).filter(Models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user with id {id} does not exit")
    user.update(updated_user.dict(), synchronize_session=False)


@app.patch("/users/{id}")
def update_hero(id: int, updated_user: UserUpdate,db: Session=Depends(get_db)):
    user = db.query(Models.User).filter(Models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = updated_user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


app.include_router(api_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")