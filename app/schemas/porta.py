from typing import Optional
from pydantic import BaseModel

class PortaSchema(BaseModel):
    id_porta: Optional[int] = None
    descricao: str
    hora: str