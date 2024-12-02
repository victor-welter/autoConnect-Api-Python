from typing import Optional
from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    id_usuario: Optional[int] = None
    nome: str
    email: str
    senha: str
    data_criacao: Optional[str] = None