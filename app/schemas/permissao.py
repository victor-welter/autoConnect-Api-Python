from typing import Optional
from pydantic import BaseModel

class PermissaoSchema(BaseModel):
    id_permissao: Optional[int] = None
    nome: str
    descricao: str