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

def update_categoria(db: Session, id_categoria: int, categoria: Categoria):
    try:
        result = db.execute(text(
            "UPDATE categoria "
            "SET descricao = :descricao "
            "WHERE id_categoria = :id_categoria"
        ), {
            "descricao": categoria.descricao,
            "id_categoria": id_categoria
        })
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar categoria: {str(e)}")

def get_categorias(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_categoria, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM categoria 
        """

        where_clause = []
        parameters = {}

        if where:
            where_clause.append("unaccent(lower(descricao)) LIKE unaccent(lower(:where))")
            parameters["where"] = f"%{where}%"

        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)
        
        base_query += f" LIMIT {limit} OFFSET {offset}"
        parameters["limit"] = limit
        parameters["offset"] = offset

        result = db.execute(text(base_query), parameters)

        return [{
            "id_categoria": row["id_categoria"],
            "descricao": row["descricao"],
        } for row in result]
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