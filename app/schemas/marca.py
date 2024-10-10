from pydantic import BaseModel

class MarcaSchema(BaseModel):
    id_marca: int
    descricao: str

    class Config:
        orm_mode = True