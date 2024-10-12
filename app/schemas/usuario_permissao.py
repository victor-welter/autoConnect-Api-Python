from pydantic import BaseModel

class UsuarioPermissaoSchema(BaseModel):
    id_usuario_permissao: int
    id_usuario: int
    id_permissao: int
    data_associacao: str

    class Config:
        orm_mode = True