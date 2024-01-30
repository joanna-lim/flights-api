from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    flights = db.query(models.Flight).all()
    return flights

def get_flight_no(flight_no:str, db: Session):
    flights = db.query(models.Flight).filter(models.Flight.flight_no==flight_no).all()
    return flights

def get_time(epoch_time:float, db:Session):
    flights = db.query(models.Flight).filter(models.Flight.epoch_time==epoch_time).all()
    return flights

def create(request:schemas.Flight, db:Session):
    new_id = str(request.epoch_time) + "_" + request.flight_no
    new_flight = models.Flight(id = new_id, flight_no = request.flight_no, epoch_time = request.epoch_time,
                               alt_baro = request.alt_baro, latitude = request.latitude, longitude = request.longitude)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight

def delete_flight(id:str, db:Session):
    flight = db.query(models.Flight).filter(models.Flight.id==id)
    if not flight.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Flight of id {id} not found")
    flight.delete(synchronize_session=False)
    db.commit()
    return 'Deleted successfully'

def delete_flight_no(flight_no:str, db:Session):
    flights = db.query(models.Flight).filter(models.Flight.flight_no==flight_no).all()
    if not flights:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Flight number {flight_no} not found")
    for flight in flights:
        db.delete(flight)
    db.commit()
    return 'Deleted successfully'

def delete_time(epoch_time:float, db:Session):
    flights = db.query(models.Flight).filter(models.Flight.epoch_time==epoch_time).all()
    if not flights:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Epoch time {epoch_time} not found")
    for flight in flights:
        db.delete(flight)
    db.commit()
    return 'Deleted successfully'
