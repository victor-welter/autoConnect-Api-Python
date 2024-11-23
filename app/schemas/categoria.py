from typing import Optional
from pydantic import BaseModel

class CategoriaSchema(BaseModel):
    id_categoria: Optional[int] = None
    descricao: str