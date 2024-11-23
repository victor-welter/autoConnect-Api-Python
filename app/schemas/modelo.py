from typing import Optional
from pydantic import BaseModel

class ModeloSchema(BaseModel):
    id_modelo: Optional[int] = None
    descricao: str