from pydantic import BaseModel

class RegistroPortaSchema(BaseModel):
    id_registro_porta: int
    estado_porta: str
    data_hora: str
    id_porta: int
