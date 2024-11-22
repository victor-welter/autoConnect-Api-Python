from pydantic import BaseModel

class DespesaSchema(BaseModel):
    id_despesa: int
    data: str
    odometro: float
    preco_unitario: float
    quantidade: float
    preco_total: float
    manutencao_preventiva: int
    descricao: str
    id_veiculo: int
    id_local: int
    id_tipo_despesa: int
    id_tipo_combustivel: int
    id_tipo_problema: int