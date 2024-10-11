from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Marca

def add_marca(db: Session, marca: Marca):
    try:
        db.execute(text(
            "INSERT INTO marca (descricao)"
            "VALUES (:descricao)"
        ), {
            "descricao": marca.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar marca: {str(e)}")

# TODO - Implementar atualização de marcas
def update_marca(db: Session, id_marca: int, marca: Marca):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar marca: {str(e)}")

# TODO - Implementar busca de marcas
def get_marcas(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar marcas: {str(e)}")

def delete_marca_by_id(db: Session, id_marca: int):
    try:
        result = db.execute(text(
            "DELETE FROM marca WHERE id_marca = :id_marca"
        ), {"id_marca": id_marca})

        db.commit()
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar marca: {str(e)}")