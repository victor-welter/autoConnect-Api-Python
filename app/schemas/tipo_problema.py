from pydantic import BaseModel

class TipoProblemaSchema(BaseModel):
    id_tipo_problema: int
    descricao: str

    class Config:
        orm_mode = True