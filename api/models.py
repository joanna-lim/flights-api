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

class Ship(Base):
    __tablename__ = 'ships'
    id = Column(String, primary_key=True, index=True) # string of epoch time + "_" + flight number
    call_sign = Column(String)
    epoch_time = Column(Float)
    speed_over_time = Column(Float)
    course_over_time = Column(Float)
    heading = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    