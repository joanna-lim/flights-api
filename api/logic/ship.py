from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    ships = db.query(models.Ship).all()
    return ships

def get_call_sign(call_sign:str, db: Session):
    ships = db.query(models.Ship).filter(models.Ship.call_sign==call_sign).all()
    return ships

def get_time(epoch_time:float, db:Session):
    ships = db.query(models.Ship).filter(models.Ship.epoch_time==epoch_time).all()
    return ships

def create(request:schemas.Ship, db:Session):
    new_id = str(request.epoch_time) + "_" + request.call_sign
    new_ship = models.Ship(id = new_id, call_sign = request.call_sign, epoch_time = request.epoch_time,
                           speed_over_time = request.speed_over_time, course_over_time = request.course_over_time, 
                           heading = request.heading, latitude = request.latitude, longitude = request.longitude)
    db.add(new_ship)
    db.commit()
    db.refresh(new_ship)
    return new_ship

def delete_ship(id:str, db:Session):
    ship = db.query(models.Ship).filter(models.Ship.id==id)
    if not ship.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Ship of id {id} not found")
    ship.delete(synchronize_session=False)
    db.commit()
    return 'Deleted successfully'

def delete_call_sign(call_sign:str, db:Session):
    ships = db.query(models.Ship).filter(models.Ship.call_sign==call_sign).all()
    if not ships:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Call sign {call_sign} not found")
    for ship in ships:
        db.delete(ship)
    db.commit()
    return 'Deleted successfully'

def delete_time(epoch_time:float, db:Session):
    ships = db.query(models.Ship).filter(models.Ship.epoch_time==epoch_time).all()
    if not ships:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Epoch time {epoch_time} not found")
    for ship in ships:
        db.delete(ship)
    db.commit()
    return 'Deleted successfully'
