from fastapi import FastAPI, HTTPException
from models import Programmer, Languages, Message
from typing import List

db: List[Programmer] = [
    Programmer(id=1, name="Dennis Ritchie", languages=[Languages.b, Languages.c]),
    Programmer(id=2, name="Brian Wilson Kernighan", languages=[Languages.c]),
    Programmer(id=3, name="James Gosling", languages=[Languages.java]),
    Programmer(id=4, name="Guido van Rossum", languages=[Languages.python]),
    Programmer(id=5, name="Brendan Eich", languages=[Languages.javascript])
]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hi/{name}", response_model=Message)
async def hi(name: str) -> Message:
    return Message(message=f"Hello, {name}")


# Programmers

@app.get("/programmers", response_model=List[Programmer])
async def get_programmers(skip: int = 0, limit: int = 5) -> list[Programmer]:
    return db[skip: skip + limit]


@app.get("/programmers/{programmer_id}", response_model=Programmer)
async def get_programmer(programmer_id: int) -> Programmer:
    response = next((programmer for programmer in db if programmer.id == programmer_id), None)

    if response is None:
        raise HTTPException(status_code=404, detail="Programmer not found")

    return response


@app.post("/programmers", response_model=Programmer)
async def create_programmer(programmer: Programmer) -> Programmer:
    db.append(programmer)
    return programmer
