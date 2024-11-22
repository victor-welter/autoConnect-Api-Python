from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import RegistroPorta

def add_registro_porta(db: Session, registro_porta: RegistroPorta):
    try:
        db.execute(text(
            "INSERT INTO registro_porta (estado_porta, data_hora, id_porta)"
            "VALUES (:estado_porta, :data_hora, :id_porta)"
        ), {
            "estado_porta": registro_porta.estado_porta,
            "data_hora": registro_porta.data_hora,
            "id_porta": registro_porta.id_porta
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar registro da porta: {str(e)}")

def update_registro_porta(db: Session, id_registro_porta: int, registro_porta: RegistroPorta):
    try:
        result = db.execute(text(
            "UPDATE registro_porta "
            "SET estado_porta = :estado_porta, "
            "data_hora = :data_hora, "
            "id_porta = :id_porta"
            "WHERE id_registro_porta = :registro_porta"
        ), {
            "estado_porta": registro_porta.estado_porta,
            "data_hora": registro_porta.data_hora,
            "id_porta": registro_porta.id_porta,
            "id_registro_porta": id_registro_porta
        })
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar registro da porta: {str(e)}")

def get_registros_porta(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_registro_porta, 
                estado_porta,
                data_hora,
                id_porta
            FROM registro_porta 
        """

        where_clause = []
        parameters = {}

        if where:
            where_clause.append("unaccent(lower(id_porta)) LIKE unaccent(lower(:where))")
            parameters["where"] = f"%{where}%"

        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)

        base_query += " LIMIT :limit OFFSET :offset"
        parameters["limit"] = limit
        parameters["offset"] = offset

        result = db.execute(text(base_query), parameters).mappings()

        return [dict(row) for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar registros da porta: {str(e)}")

def delete_registro_porta_by_id(db: Session, id_registro_porta: int):
    try:
        result = db.execute(text(
            "DELETE FROM registro_porta WHERE id_registro_porta = :id_registro_porta"
        ), {"id_registro_porta": id_registro_porta})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar registro da porta: {str(e)}")