from typing import Optional
from pydantic import BaseModel

class RegistroCombustivelSchema(BaseModel):
    id_registro_combustivel: Optional[int] = None
    voltagem: float
    data_hora: Optional[str] = None
    id_veiculo: int
    quantidade_combustivel: Optional[float] = None
    porcentagem_combustivel: Optional[float] = None
