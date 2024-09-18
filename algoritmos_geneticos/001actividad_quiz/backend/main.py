from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = [
    "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins)

class Population(BaseModel):
    songRating: float
    songPopularity: float
    songDuration: float
    songEnergy: float
    songDanceability: float
    songLoudness: float
    @property
    def songRating(self):
        return self._songRating
    @property
    def songPopularity(self):
        return self._songPopularity
    @property
    def songDuration(self):
        return self._songDuration
    @property
    def songEnergy(self):
        return self._songEnergy
    @property
    def songDanceability(self):
        return self._songDanceability
    @property
    def songLoudness(self):
        return self._songLoudness


@app.get("/health")
def read_root():
    return {"status": "ok!"}  

@app.post("/evaluate")
def evaluate_population(population: Population):
    print("Evaluando población")
    return f'danceability: {population.songDanceability}, \n songDuration: {population.songDuration}, \n songEnergy: {population.songEnergy}, \n songLoudness: {population.songLoudness}, \n songPopularity: {population.songPopularity}, \n songRating: {population.songRating}'