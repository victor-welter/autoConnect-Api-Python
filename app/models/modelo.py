from sqlalchemy import Column, Integer, String
from app.database import Base

class Modelo(Base):
    __tablename__ = 'modelo'

    id_modelo = Column(Integer, primary_key=True, index=True)
    id_marca = Column(Integer, index=True)
    descricao = Column(String)