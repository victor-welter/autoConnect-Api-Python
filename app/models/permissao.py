from sqlalchemy import Column, Integer, String
from app.database import Base

class Permissao(Base):
    __tablename__ = 'permissao'

    id_permissao = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)