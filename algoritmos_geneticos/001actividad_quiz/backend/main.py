from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algoritmo_genetico import genetic_algorithm
import algoritmo_genetico


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

class Population(BaseModel):
    preferredGenre: str
    mood: str


@app.get("/health")
def read_root():
    return {"status": "ok!"}  

@app.post("/evaluate")
def evaluate_population(population: Population):
    print("Evaluando población")
    return genetic_algorithm(population.preferredGenre, population.mood)

@app.get("/genres")
def get_genres():
    return algoritmo_genetico.get_genres()

@app.get("/moods")
def get_moods():
    return algoritmo_genetico.get_moods()
