from typing import Optional
from pydantic import BaseModel

class UsuarioPermissaoSchema(BaseModel):
    id_usuario_permissao: Optional[int] = None
    id_usuario: int
    id_permissao: int
    data_associacao: str