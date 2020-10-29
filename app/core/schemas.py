from typing import Tuple, Optional
from datetime import datetime
from pydantic import BaseModel, Field
import uuid as pyuuid


class BaseDataModel(BaseModel):
    name: str
    timestamp: datetime
    coord: Optional[str]
    data: dict
    uuid: pyuuid.UUID


class GPS(BaseDataModel):
    class Config:
        orm_mode = True


class Temperature(BaseDataModel):
    class Config:
        orm_mode = True

