from sqlalchemy import Column, Integer, DateTime, String
from app.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    data_criacao = Column(DateTime)
