from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import volumen_level_logica_difusa as vld

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

class UserDetails(BaseModel):
    mood: float
    hour: float

@app.post("/evaluate")
async def evaluate(UserDetails: UserDetails):
    buf = vld.evaluate_(UserDetails.hour, UserDetails.mood)
    return Response(content=buf.getvalue(), media_type="image/png")

@app.get("/visualizacion_hour")
async def visualizacion_hour():
    buf = vld.visualizacion_hour()
    return Response(content=buf.getvalue(), media_type="image/png")

@app.get("/visualizacion_mood")
async def visualizacion_mood():
    buf = vld.visualizacion_mood()
    return Response(content=buf.getvalue(), media_type="image/png")



