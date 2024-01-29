from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from .. import schemas, database
from typing import List
from ..logic import flight

router = APIRouter(
    prefix='/flight',
    tags =['Flights']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.Flight]) 
def get_all(db:Session = Depends(get_db)):
    return flight.get_all(db)

@router.get('/flightno/{flight_no}', response_model=List[schemas.Flight]) 
def get_flight_no(flight_no:str, db:Session = Depends(get_db)):
    return flight.get_flight_no(flight_no, db)

@router.get('/time/{epoch_time}', response_model=List[schemas.Flight]) 
def get_flight_no(epoch_time:float, db:Session = Depends(get_db)):
    return flight.get_time(epoch_time, db)

@router.post('/', status_code=status.HTTP_201_CREATED) 
def create(request: schemas.Flight, db:Session = Depends(get_db)):
    return flight.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_flight(id:str, db:Session = Depends(get_db)):
    return flight.delete_flight(id, db)

@router.delete('/flightno/{flight_no}', status_code = status.HTTP_204_NO_CONTENT)
def delete_flight_no(flight_no:str, db:Session = Depends(get_db)):
    return flight.delete_flight_no(flight_no, db)

@router.delete('/time/{epoch_time}', status_code = status.HTTP_204_NO_CONTENT)
def delete_flight_no(epoch_time:float, db:Session = Depends(get_db)):
    return flight.delete_time(epoch_time, db)

