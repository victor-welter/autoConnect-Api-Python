from typing import Optional
from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    id_veiculo: Optional[int] = None
    ano: str
    placa: str
    cor: str
    odometro: float
    voltagem_min: float
    voltagem_max: float
    id_marca: int
    id_modelo: int
    id_usuario: int