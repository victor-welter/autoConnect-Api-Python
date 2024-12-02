from typing import Optional
from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    id_veiculo: Optional[int] = None
    ano: str
    placa: str
    cor: str
    odometro: float
    capacidade_tanque: Optional[float] = None
    voltagem_min: Optional[float] = None
    voltagem_max: Optional[float] = None
    id_marca: int
    id_modelo: int
    id_usuario: int