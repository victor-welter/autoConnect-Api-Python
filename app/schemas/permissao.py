from pydantic import BaseModel

class PermissaoSchema(BaseModel):
    id_permissao: int
    nome: str
    descricao: str

    class Config:
        orm_mode = True