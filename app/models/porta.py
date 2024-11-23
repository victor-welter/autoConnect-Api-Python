from sqlalchemy import Column, Integer, String
from app.database import Base

class Porta(Base):
    __tablename__ = 'porta'

    id_porta = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    hora = Column(String)