from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Porta

def add_porta(db: Session, porta: Porta):
    try:
        db.execute(text(
            "INSERT INTO porta (descricao, hora)"
            "VALUES (:descricao, :hora)"
        ), {
            "descricao": porta.descricao,
            "hora": porta.hora,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar porta: {str(e)}")

def update_porta(db: Session, porta: Porta):
    try:
        result = db.execute(text(
            "UPDATE porta "
            "SET descricao = :descricao, hora = :hora "
            "WHERE id_porta = :id_porta"
        ), {
            "descricao": porta.descricao,
            "hora": porta.hora,
            "id_porta": porta.id_porta
        })
        db.commit()
        
        print(f"Linhas afetadas: {result.rowcount}")
        
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar porta: {str(e)}")

def get_portas(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_porta, 
                descricao,
                hora
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

def get_porta_by_id(db: Session, id_porta: int):
    try:
        result = db.execute(text(
            "SELECT id_porta, descricao, hora FROM porta WHERE id_porta = :id_porta"
        ), {"id_porta": id_porta}).mappings().first()

        return dict(result)
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar porta por ID: {str(e)}")

def delete_porta_by_id(db: Session, id_porta: int):
    try:
        result = db.execute(text(
            "DELETE FROM porta WHERE id_porta = :id_porta"
        ), {"id_porta": id_porta})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar porta: {str(e)}")