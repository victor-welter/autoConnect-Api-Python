from pydantic import BaseModel
from typing import List

class EmailSchema(BaseModel):
    destinatarios_email: List[str]
    assunto: str
    corpo_email: str