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

def update_tipo_problema(db: Session, id_tipo_problema: int, tipo_problema: TipoProblema):
    try:
        result = db.execute(text(
            "UPDATE tipo_problema "
            "SET descricao = :descricao "
            "WHERE id_tipo_problema = :id_tipo_problema"
        ), {
            "descricao": tipo_problema.descricao,
            "id_tipo_problema": id_tipo_problema
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar tipo de problema: {str(e)}")

def get_tipos_problema(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_tipo_problema, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM tipo_problema 
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
            "id_tipo_problema": row["id_tipo_problema"],
            "descricao": row["descricao"]
        } for row in result]
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