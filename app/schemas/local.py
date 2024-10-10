from pydantic import BaseModel

class LocalSchema(BaseModel):
    id_local: int
    id_categoria: int
    nome: str
    endereco: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True