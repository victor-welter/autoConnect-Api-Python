from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import TipoProblema

def add_tipo_problema(db: Session, tipo_problema: TipoProblema):
    try:
        db.execute(text(
            "INSERT INTO tipo_problema (descricao) "
            "VALUES (:descricao)"
        ), {
            "descricao": tipo_problema.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar tipo de problema: {str(e)}")

# TODO - Implementar atualização de tipos de problema
def update_tipo_problema(db: Session, id_tipo_problema: int, tipo_problema: TipoProblema):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar tipo de problema: {str(e)}")

# TODO - Implementar busca de tipos de problema
def get_tipos_problema(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar tipos de problema: {str(e)}")

def delete_tipo_problema_by_id(db: Session, id_tipo_problema: int):
    try:
        result = db.execute(text(
            "DELETE FROM tipo_problema WHERE id_tipo_problema = :id_tipo_problema"
        ), {"id_tipo_problema": id_tipo_problema})

        db.commit()
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar tipo de problema: {str(e)}")