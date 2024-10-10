from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoCombustivel(Base):
    __tablename__ = 'tipo_combustivel'

    id_tipo_combustivel = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)