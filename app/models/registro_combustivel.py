from sqlalchemy import Column, Integer, Float, DateTime
from app.database import Base

class RegistroCombustivel(Base):
    __tablename__ = 'registro_combustivel'

    id_registro_combustivel = Column(Integer, primary_key=True, index=True)
    voltagem = Column(Float)
    data_hora = Column(DateTime)
    id_veiculo = Column(Integer, index=True)