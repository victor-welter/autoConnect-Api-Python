from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    id_veiculo: int
    ano: str
    placa: str
    odometro: float
    id_marca: int
    id_modelo: int

    class Config:
        orm_mode = True