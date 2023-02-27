from fastapi import FastAPI
from typing import List, Dict
from pydantic import BaseModel


class Item(BaseModel):
    item_name : str
    price : int


app = FastAPI()

items = [
    {
        "item_name" : "banana",
        "price" : 60
    },
    {
        "item_name" : "cake",
        "price" : 100
    },
    {
        "item_name" : "chocolate",
        "price" : 80
    }
]


@app.get("/", status_code=200)
def root():
    return {'message: hello'}

#post method because of list lenghth
@app.post('/total/', status_code=201)
async def sum(items: List[Item]):
    total : int= 0
    for object in items:
        total += object.price
    return total


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
