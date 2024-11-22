from sqlalchemy import Column, Integer, String
from app.database import Base

class RegistroPorta(Base):
    __tablename__ = 'registro_porta'

    id_registro_porta = Column(Integer, primary_key=True, index=True)
    estado_porta = Column(String)
    data_hora = Column()
    id_porta = Column(Integer, index=True)