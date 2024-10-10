from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Categoria

def add_categoria(db: Session, categoria: Categoria):
    try:
        db.execute(text(
            "INSERT INTO categoria (descricao)"
            "VALUES (:descricao)"
        ), {
            "descricao": categoria.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar categoria: {str(e)}")

# TODO - Implementar atualização de categorias
def update_categoria(db: Session, id_categoria: int, categoria: Categoria):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar categoria: {str(e)}")

# TODO - Implementar busca de categorias
def get_categorias(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar categorias: {str(e)}")

def delete_categoria_by_id(db: Session, id_categoria: int):
    try:
        result = db.execute(text(
            "DELETE FROM categoria WHERE id_categoria = :id_categoria"
        ), {"id_categoria": id_categoria})

        db.commit()
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar categoria: {str(e)}")