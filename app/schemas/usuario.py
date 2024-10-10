from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    id_usuario: int
    nome: str
    email: str
    senha: str
    data_criacao: str

    class Config:
        orm_mode = True