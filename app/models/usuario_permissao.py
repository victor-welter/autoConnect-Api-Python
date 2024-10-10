from sqlalchemy import Column, Integer, DateTime
from app.database import Base

class UsuarioPermissao(Base):
    __tablename__ = 'usuario_permissao'

    id_usuario_permissao = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, index=True)
    id_permissao = Column(Integer, index=True)
    data_associacao = Column(DateTime)