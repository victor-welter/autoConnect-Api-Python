from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoProblema(Base):
    __tablename__ = 'tipos_problema'

    id_tipo_problema = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)