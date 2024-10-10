from pydantic import BaseModel

class ModeloSchema(BaseModel):
    id_modelo: int
    descricao: str

    class Config:
        orm_mode = True