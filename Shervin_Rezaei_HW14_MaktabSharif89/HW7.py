from fastapi import FastAPI
from typing import List


app = FastAPI()


@app.get("/", status_code=200)
def root():
    return {'message: Hi'}


@app.post('/evenSumation/', status_code=201)
async def sum_of_evens(list_of_numbers: List[int]):
    sum = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            sum += number
    return sum


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug") 
