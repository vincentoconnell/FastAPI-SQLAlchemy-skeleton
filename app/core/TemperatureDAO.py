from sqlalchemy.orm import Session
from . import models
from datetime import datetime
import pandas as pd

def get_temp(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Temperature).offset(offset).limit(limit).all()

def get_temp_by_date_range(db: Session, startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 0):
    return db.query(models.Temperature).filter(models.Temperature.timestamp < enddate)\
            .filter(models.Temperature.timestamp > startdate).offset(offset).limit(limit).all()

def get_temp_by_date_range_as_dataframe(db: Session, startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 0):
    return pd.read_sql(db.query(models.Temperature).filter(models.Temperature.timestamp < enddate)\
        .filter(models.Temperature.timestamp > startdate).offset(offset).limit(limit).statement, db.bind)

def get_temp_for_name_by_date_range_as_dataframe(
        db: Session,
        name: str,
        startdate: datetime,
        enddate: datetime,
        offset: int = 0,
        limit: int = 0):
    return pd.read_sql(db.query(models.Temperature)\
        .filter(models.Temperature.name == name)\
        .filter(models.Temperature.timestamp < enddate)\
        .filter(models.Temperature.timestamp > startdate)
        .offset(offset).limit(limit).statement, db.bind)
