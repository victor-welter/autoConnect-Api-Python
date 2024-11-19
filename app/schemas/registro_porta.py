from pydantic import BaseModel

class RegistroPortaSchema(BaseModel):
    id_registro_porta: int
    descricao: str

    class Config:
        orm_mode = True