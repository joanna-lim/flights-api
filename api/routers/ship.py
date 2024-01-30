from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from .. import schemas, database
from typing import List
from ..logic import ship

router = APIRouter(
    prefix='/ship',
    tags =['Ships']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.Ship]) 
def get_all(db:Session = Depends(get_db)):
    return ship.get_all(db)

@router.get('/callsign/{call_sign}', response_model=List[schemas.Ship]) 
def get_call_sign(call_sign:str, db:Session = Depends(get_db)):
    return ship.get_call_sign(call_sign, db)

@router.get('/time/{epoch_time}', response_model=List[schemas.Ship]) 
def get_time(epoch_time:float, db:Session = Depends(get_db)):
    return ship.get_time(epoch_time, db)

@router.post('/', status_code=status.HTTP_201_CREATED) 
def create(request: schemas.Ship, db:Session = Depends(get_db)):
    return ship.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_ship(id:str, db:Session = Depends(get_db)):
    return ship.delete_ship(id, db)

@router.delete('/callsign/{call_sign}', status_code = status.HTTP_204_NO_CONTENT)
def delete_call_sign(call_sign:str, db:Session = Depends(get_db)):
    return ship.delete_call_sign(call_sign, db)

@router.delete('/time/{epoch_time}', status_code = status.HTTP_204_NO_CONTENT)
def delete_time(epoch_time:float, db:Session = Depends(get_db)):
    return ship.delete_time(epoch_time, db)

