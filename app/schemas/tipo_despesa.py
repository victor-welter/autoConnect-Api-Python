from typing import Optional
from pydantic import BaseModel

class TipoDespesaSchema(BaseModel):
    id_tipo_despesa: Optional[int] = None
    descricao: str