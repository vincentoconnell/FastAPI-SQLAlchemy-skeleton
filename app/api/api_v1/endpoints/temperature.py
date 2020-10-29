from app.core import TemperatureDAO, schemas
from app.core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi import APIRouter
from datetime import datetime


router = APIRouter()

@router.get("/temperaturetest", response_model=List[schemas.Temperature])
async def temp_get_test(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    temps = TemperatureDAO.get_temp(db, offset=offset, limit=limit)
    return temps

@router.get("/temp", response_model=List[schemas.Temperature])
async def temp_get(startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    temps = TemperatureDAO.get_temp_by_date_range(db, startdate, enddate, offset=offset, limit=limit)
    return temps