from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Porta

def add_porta(db: Session, porta: Porta):
    try:
        db.execute(text(
            "INSERT INTO porta (descricao)"
            "VALUES (:descricao)"
        ), {
            "descricao": porta.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar porta: {str(e)}")

def update_porta(db: Session, id_porta: int, porta: Porta):
    try:
        result = db.execute(text(
            "UPDATE porta "
            "SET descricao = :descricao "
            "WHERE id_porta = :id_porta"
        ), {
            "descricao": porta.descricao,
            "id_porta": id_porta
        })
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar porta: {str(e)}")

def get_portas(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_porta, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM porta 
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
        raise DatabaseError(f"Erro ao buscar portas: {str(e)}")

def delete_porta_by_id(db: Session, id_porta: int):
    try:
        result = db.execute(text(
            "DELETE FROM porta WHERE id_porta = :id_porta"
        ), {"id_porta": id_porta})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar porta: {str(e)}")