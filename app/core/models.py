from .database import Base
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import configure_mappers


class BaseDataModel(AbstractConcreteBase, Base):
    name = Column(String)
    timestamp = Column(DATETIME)
    coord = Column(String)
    data = Column(JSONB)
    uuid = Column(UUID, primary_key=True, index=True)


class GPS(BaseDataModel):
    __tablename__ = "gps"
    __mapper_args__ = {
        'polymorphic_identity': 'gps',
        'concrete': True
    }


class Temperature(BaseDataModel):
    __tablename__ = "temperature"
    __mapper_args__ = {
        'polymorphic_identity': 'temperature',
        'concrete': True
    }


configure_mappers()
