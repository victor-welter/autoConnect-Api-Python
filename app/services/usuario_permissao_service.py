from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Local

def add_local(db: Session, local: Local):
    try:
        db.execute(text(
            "INSERT INTO local (descricao)"
            "VALUES (:descricao)"
        ), {
            "descricao": local.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar local: {str(e)}")

# TODO - Implementar atualização de locais
def update_local(db: Session, id_local: int, local: Local):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar local: {str(e)}")

# TODO - Implementar busca de locais
def get_locais(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar locais: {str(e)}")

def delete_local_by_id(db: Session, id_local: int):
    try:
        result = db.execute(text(
            "DELETE FROM local WHERE id_local = :id_local"
        ), {"id_local": id_local})

        db.commit()
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar local: {str(e)}")