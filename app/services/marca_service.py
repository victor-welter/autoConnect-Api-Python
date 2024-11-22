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

def update_marca(db: Session, id_marca: int, marca: Marca):
    try:
        result = db.execute(text(
            "UPDATE marca "
            "SET descricao = :descricao "
            "WHERE id_marca = :id_marca"
        ), {
            "descricao": marca.descricao,
            "id_marca": id_marca
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar marca: {str(e)}")

def get_marcas(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_marca, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM marca 
        """

        where_clause = []
        parameters = {}

        if where:
            where_clause.append("unaccent(lower(descricao)) LIKE unaccent(lower(:where))")
            parameters["where"] = f"%{where}%"

        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)
        
        base_query += " LIMIT :limit OFFSET :offset"
        parameters["limit"] = limit
        parameters["offset"] = offset

        result = db.execute(text(base_query), parameters).mappings()

        return [dict(row) for row in result]
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