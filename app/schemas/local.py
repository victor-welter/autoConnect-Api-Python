from typing import Optional
from pydantic import BaseModel

class LocalSchema(BaseModel):
    id_categoria: Optional[int] = None
    nome: str
    endereco: str
    latitude: float
    longitude: float