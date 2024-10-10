from pydantic import BaseModel

class CategoriaSchema(BaseModel):
    id_categoria: int
    descricao: str

    class Config:
        orm_mode = True