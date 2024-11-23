from typing import Optional
from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    id_veiculo: Optional[int] = None
    ano: str
    placa: str
    odometro: float
    id_marca: int
    id_modelo: int