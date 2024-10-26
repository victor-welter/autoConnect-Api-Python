from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import TipoCombustivel

def add_tipo_combustivel(db: Session, tipo_combustivel: TipoCombustivel):
    try:
        db.execute(text(
            "INSERT INTO tipo_combustivel (descricao) "
            "VALUES (:descricao)"
        ), {
            "descricao": tipo_combustivel.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar tipo de combustível: {str(e)}")

def update_tipo_combustivel(db: Session, id_tipo_combustivel: int, tipo_combustivel: TipoCombustivel):
    try:
        result = db.execute(text(
            "UPDATE tipo_combustivel "
            "SET descricao = :descricao "
            "WHERE id_tipo_combustivel = :id_tipo_combustivel"
        ), {
            "descricao": tipo_combustivel.descricao,
            "id_tipo_combustivel": id_tipo_combustivel
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar tipo de combustível: {str(e)}")

def get_tipos_combustivel(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_tipo_combustivel, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM tipo_combustivel 
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
            "id_tipo_combustivel": row["id_tipo_combustivel"],
            "descricao": row["descricao"]
        } for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar tipos de combustível: {str(e)}")

def delete_tipo_combustivel_by_id(db: Session, id_tipo_combustivel: int):
    try:
        result = db.execute(text(
            "DELETE FROM tipo_combustivel WHERE id_tipo_combustivel = :id_tipo_combustivel"
        ), {"id_tipo_combustivel": id_tipo_combustivel})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar tipo de combustível: {str(e)}")