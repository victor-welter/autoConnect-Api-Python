from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import TipoDespesa

def add_tipo_despesa(db: Session, tipo_despesa: TipoDespesa):
    try:
        db.execute(text(
            "INSERT INTO tipo_despesa (descricao) "
            "VALUES (:descricao)"
        ), {
            "descricao": tipo_despesa.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar tipo de despesa: {str(e)}")

# TODO - Implementar atualização de tipos de despesa
def update_tipo_despesa(db: Session, id_tipo_despesa: int, tipo_despesa: TipoDespesa):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar tipo de despesa: {str(e)}")

# TODO - Implementar busca de tipos de despesa
def get_tipos_despesa(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar tipos de despesa: {str(e)}")

def delete_tipo_despesa_by_id(db: Session, id_tipo_despesa: int):
    try:
        result = db.execute(text(
            "DELETE FROM tipo_despesa WHERE id_tipo_despesa = :id_tipo_despesa"
        ), {"id_tipo_despesa": id_tipo_despesa})

        db.commit()
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar tipo de despesa: {str(e)}")