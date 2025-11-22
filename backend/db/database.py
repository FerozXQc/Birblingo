from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///birblingo.db",echo=True)

