from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer

class Base(DeclarativeBase):
    pass

class TestModel(Base):
    __tablename__ = "test"
    id = Column(Integer,auto_increment=True, primary_key=True)
    name = Column(String)