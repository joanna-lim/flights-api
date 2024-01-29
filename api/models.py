from sqlalchemy import Column, String, Float
from .database import Base

# sql models

class Flight(Base):
    __tablename__ = 'flights'
    id = Column(String, primary_key=True, index=True) # string of epoch time + "_" + flight number
    flight_no = Column(String)
    epoch_time = Column(Float)
    alt_baro = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)