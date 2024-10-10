from pydantic import BaseModel

class TipoCombustivelSchema(BaseModel):
    id_tipo_combustivel: int
    descricao: str

    class Config:
        orm_mode = True