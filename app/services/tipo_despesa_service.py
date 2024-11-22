from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import TipoDespesa

def add_tipo_despesa(db: Session, tipo_despesa: TipoDespesa):
    try:
        db.execute(text(
            "INSERT INTO tipo_despesa (descricao) "
            "VALUES (:descricao)"
        ), {
            "descricao": tipo_despesa.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar tipo de despesa: {str(e)}")

def update_tipo_despesa(db: Session, id_tipo_despesa: int, tipo_despesa: TipoDespesa):
    try:
        result = db.execute(text(
            "UPDATE tipo_despesa "
            "SET descricao = :descricao "
            "WHERE id_tipo_despesa = :id_tipo_despesa"
        ), {
            "descricao": tipo_despesa.descricao,
            "id_tipo_despesa": id_tipo_despesa
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar tipo de despesa: {str(e)}")

def get_tipos_despesa(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_tipo_despesa, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM tipo_despesa 
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
        raise DatabaseError(f"Erro ao buscar tipos de despesa: {str(e)}")

def delete_tipo_despesa_by_id(db: Session, id_tipo_despesa: int):
    try:
        result = db.execute(text(
            "DELETE FROM tipo_despesa WHERE id_tipo_despesa = :id_tipo_despesa"
        ), {"id_tipo_despesa": id_tipo_despesa})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar tipo de despesa: {str(e)}")