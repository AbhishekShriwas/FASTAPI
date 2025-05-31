from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Root route
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Request body model for POST
class NumberInput(BaseModel):
    number: int

# Correct POST route to get the square of a number
@app.post("/get_square")
async def get_square(input: NumberInput):
    return {"square": input.number ** 2}

# Route with path parameter
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

