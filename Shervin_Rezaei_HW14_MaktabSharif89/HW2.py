from fastapi import FastAPI,HTTPException

app = FastAPI()


books = [
    {
        "bookName" : "Big Magic", 
        "description" : "Elizabeth Gilbert is a best-selling author and this is her creative manifesto. She believes that you should show up and push through the inevitable self-doubt. Stay focused, find joy in what you are doing. As long as you keep going, you will be rewarded by  the “strange jewels” of inspiration and magic that she believes is in all of us. "
    },
    {
        "bookName" : "Breakfast with Buddha", 
        "description" : " Breakfast with Buddha is a novel, but it deals with the human condition and life choices because an unexpected pair of men, one, a successful businessman, and the other (a homeless man) go on a journey through modern America."
    },
    {
        "bookName" : "Atomic Habits", 
        "description" : "James Clear, an expert on habit formation, reveals practical strategies that will teach you how to form good habits, break bad ones, and master the tiny behaviors that lead to remarkable results. "
    },
    {
        "bookName" : "David and Goliath", 
        "description" : " Malcolm Gladwell takes the Biblical story as his central metaphor and says that by rights David shouldn’t have won.This book will help you understand that nothing is too big for you to handle."
    }
]


@app.get("/", status_code=200)
def root():
    return {'message: Hi'}


@app.get('/search/{term}', status_code=201)
async def search(term: str):
    bookList = []
    for dic in books:
        for key, value in dic.items():
            if term.lower() in key.lower() or term.lower() in value.lower():
                bookList.append(dic)
                break
    if bookList :
        print("Found it!")
        return bookList
    else:
        raise HTTPException(
            status_code=404,
            detail="query not found"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug") 
