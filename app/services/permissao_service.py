from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Permissao

def add_permissao(db: Session, permissao: Permissao):
    try:
        db.execute(text(
            "INSERT INTO permissao (descricao) "
            "VALUES (:descricao)"
        ), {
            "descricao": permissao.descricao,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar permissão: {str(e)}")

def update_permissao(db: Session, id_permissao: int, permissao: Permissao):
    try:
        result = db.execute(text(
            "UPDATE permissao "
            "SET descricao = :descricao "
            "WHERE id_permissao = :id_permissao"
        ), {
            "descricao": permissao.descricao,
            "id_permissao": id_permissao
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar permissão: {str(e)}")

def get_permissoes(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_permissao, 
                regexp_replace(COALESCE(descricao, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS descricao
            FROM permissao 
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
            "id_permissao": row["id_permissao"],
            "descricao": row["descricao"]
        } for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar permissões: {str(e)}")

def delete_permissao_by_id(db: Session, id_permissao: int):
    try:
        result = db.execute(text(
            "DELETE FROM permissao WHERE id_permissao = :id_permissao"
        ), {"id_permissao": id_permissao})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar permissão: {str(e)}")