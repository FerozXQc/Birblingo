from database import engine
from models import Base,TestModel
Base.metadata.create_all(engine)