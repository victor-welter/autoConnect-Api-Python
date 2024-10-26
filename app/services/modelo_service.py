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

def update_modelo(db: Session, id_modelo: int, modelo: Modelo):
    try:
        result = db.execute(text(
            "UPDATE modelo "
            "SET descricao = :descricao, id_marca = :id_marca "
            "WHERE id_modelo = :id_modelo"
        ), {
            "descricao": modelo.descricao,
            "id_marca": modelo.id_marca,
            "id_modelo": id_modelo
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar modelo: {str(e)}")

def get_modelos(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_modelo, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao,
                id_marca
            FROM modelo 
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
            "id_modelo": row["id_modelo"],
            "descricao": row["descricao"],
            "id_marca": row["id_marca"]
        } for row in result]
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