from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def get_gps(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.GPS).offset(offset).limit(limit).all()

def get_gps_by_date_range(db: Session, startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 0):
    return db.query(models.GPS).filter(models.GPS.timestamp < enddate).filter(models.GPS.timestamp > startdate).offset(offset).limit(limit).all()