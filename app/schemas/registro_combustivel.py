from typing import Optional
from pydantic import BaseModel

class RegistroCombustivelSchema(BaseModel):
    id_registro_combustivel: Optional[int] = None
    voltagem: float
    data_hora: str
    id_veiculo: int
