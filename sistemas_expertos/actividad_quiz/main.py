from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserDetails(BaseModel):
    name: str
    prefered_genre: str
    mood: str

@app.get("/health")
async def evaluate():
    return {"result": "ok"}

@app.post("/evaluate")
async def evaluate(user_details: UserDetails):
    return user_details
