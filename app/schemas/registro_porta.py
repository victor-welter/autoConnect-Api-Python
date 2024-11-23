from typing import Optional
from pydantic import BaseModel

class RegistroPortaSchema(BaseModel):
    id_registro_porta: Optional[int] = None
    estado_porta: str
    data_hora: str
    id_porta: int
