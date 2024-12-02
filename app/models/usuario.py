from sqlalchemy import Column, Integer, DateTime, String
from app.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    data_criacao = Column(DateTime)
