from pydantic import BaseModel

class TipoDespesaSchema(BaseModel):
    id_tipo_despesa: int
    descricao: str

    class Config:
        orm_mode = True