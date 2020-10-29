from app.core import GPSDAO, schemas
from app.core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi import APIRouter
from datetime import datetime


router = APIRouter()

@router.get("/gpstest", response_model=List[schemas.GPS])
async def gps_get_test(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gpses = GPSDAO.get_gps(db, offset=offset, limit=limit)
    return gpses

@router.get("/gps", response_model=List[schemas.GPS])
async def gps_get(startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gpses = GPSDAO.get_gps_by_date_range(db, startdate, enddate, offset=offset, limit=limit)
    return gpses