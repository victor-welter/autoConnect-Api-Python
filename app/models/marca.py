from sqlalchemy import Column, Integer, String
from app.database import Base

class Marca(Base):
    __tablename__ = 'marca'

    id_marca = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)