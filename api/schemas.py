from pydantic import BaseModel
from typing import List

# pydantic models

class Flight(BaseModel):
    flight_no: str
    epoch_time: float
    alt_baro: float
    latitude: float
    longitude: float
    class Config():
        orm_mode = True