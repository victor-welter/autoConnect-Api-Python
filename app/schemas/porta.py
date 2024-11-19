from pydantic import BaseModel

class PortaSchema(BaseModel):
    id_porta: int
    descricao: str

    class Config:
        orm_mode = True