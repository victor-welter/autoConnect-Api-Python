from sqlalchemy import Column, Integer, Float, String, DateTime
from app.database import Base

class Despesa(Base):
    __tablename__ = 'despesa'

    id_despesa = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime)
    odometro = Column(Float)
    preco_unitario = Column(Float)
    quantidade = Column(Float)
    preco_total = Column(Float)
    manutencao_preventiva = Column(Integer)
    descricao = Column(String)
    id_veiculo = Column(Integer, index=True)
    id_local = Column(Integer, index=True)
    id_tipo_despesa = Column(Integer, index=True)
    id_tipo_combustivel = Column(Integer, index=True)
    id_tipo_problema = Column(Integer, index=True)