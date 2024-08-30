from fastapi import FastAPI
from pydantic import BaseModel
import music_expert_system as mus
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

class UserDetails(BaseModel):
    name: str
    prefered_genre: str
    mood: str

@app.get("/moods")
async def get_moods():
    return {"moods": mus.moods}

@app.get("/genres")
async def get_genres():
    return {"genres": mus.genres}

@app.get("/health")
async def evaluate():
    return {"result": "ok"}

@app.post("/evaluate")
async def evaluate(user_details: UserDetails):
    return mus.evaluacion(user_details.name, user_details.prefered_genre, user_details.mood)
