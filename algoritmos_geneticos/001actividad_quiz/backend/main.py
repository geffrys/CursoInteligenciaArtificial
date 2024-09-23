from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algoritmo_genetico import genetic_algorithm
import algoritmo_genetico


app = FastAPI()

origins = [
    "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins)

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
