from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Veiculo(Base):
    __tablename__ = 'veiculo'

    id_veiculo = Column(Integer, primary_key=True, index=True)
    ano = Column(String)
    placa = Column(String)
    cor = Column(String)
    odometro = Column(Float)
    voltagem_min = Column(Float)
    voltagem_max = Column(Float)
    id_marca = Column(Integer, index=True)
    id_modelo = Column(Integer, index=True)
    id_usuario = Column(Integer, index=True)