from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Modelo

def add_modelo(db: Session, modelo: Modelo):
    try:
        db.execute(text(
            "INSERT INTO modelo (descricao, id_marca) "
            "VALUES (:descricao, :id_marca)"
        ), {
            "descricao": modelo.descricao,
            "id_marca": modelo.id_marca
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar modelo: {str(e)}")

# TODO - Implementar atualização de modelos
def update_modelo(db: Session, id_modelo: int, modelo: Modelo):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar modelo: {str(e)}")

# TODO - Implementar busca de modelos
def get_modelos(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar modelos: {str(e)}")

def delete_modelo_by_id(db: Session, id_modelo: int):
    try:
        result = db.execute(text(
            "DELETE FROM modelo WHERE id_modelo = :id_modelo"
        ), {"id_modelo": id_modelo})

        db.commit()
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar modelo: {str(e)}")