from fastapi import FastAPI
from . import models
from .database import engine
from .routers import flight, ship

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(flight.router)
app.include_router(ship.router)