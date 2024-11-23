from typing import Optional
from pydantic import BaseModel

class TipoProblemaSchema(BaseModel):
    id_tipo_problema: Optional[int] = None
    descricao: str