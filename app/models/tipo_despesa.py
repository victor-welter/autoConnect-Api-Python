from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoDespesa(Base):
    __tablename__ = 'tipo_despesa'

    id_tipo_despesa = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)