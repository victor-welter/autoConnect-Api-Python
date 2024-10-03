from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Local(Base):
    __tablename__ = 'local'

    id_local = Column(Integer, primary_key=True, index=True)
    id_categoria = Column(Integer, index=True)
    nome = Column(String)
    endereco = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)