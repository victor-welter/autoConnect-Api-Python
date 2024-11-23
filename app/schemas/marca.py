from typing import Optional
from pydantic import BaseModel

class MarcaSchema(BaseModel):
    id_marca: Optional[int] = None
    descricao: str