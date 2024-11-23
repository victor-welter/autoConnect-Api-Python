from typing import Optional
from pydantic import BaseModel

class TipoCombustivelSchema(BaseModel):
    id_tipo_combustivel: Optional[int] = None
    descricao: str