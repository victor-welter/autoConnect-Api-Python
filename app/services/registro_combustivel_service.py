from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import RegistroCombustivel

def add_registro_combustivel(db: Session, registro_combustivel: RegistroCombustivel):
    try:
        db.execute(text(
            "INSERT INTO registro_combustivel (voltagem, data_hora, id_veiculo)"
            "VALUES (:voltagem, :data_hora, :id_veiculo)"
        ), {
            "voltagem": registro_combustivel.voltagem,
            "data_hora": registro_combustivel.data_hora,
            "id_veiculo": registro_combustivel.id_veiculo
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar registro de combustível: {str(e)}")

def update_registro_combustivel(db: Session, id_registro_combustivel: int, registro_combustivel: RegistroCombustivel):
    try:
        result = db.execute(text(
            "UPDATE registro_combustivel "
            "SET voltagem = :voltagem, data_hora = :data_hora, id_veiculo = :id_veiculo "
            "WHERE id_registro_combustivel = :id_registro_combustivel"
        ), {
            "voltagem": registro_combustivel.voltagem,
            "data_hora": registro_combustivel.data_hora,
            "id_veiculo": registro_combustivel.id_veiculo,
            "id_registro_combustivel": id_registro_combustivel
        })
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar registro de combustível: {str(e)}")

def get_registros_combustivel(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_registro_combustivel,
                voltagem,
                data_hora,
                id_veiculo
            FROM registro_combustivel
        """

        where_clause = []
        parameters = {}

        if where:
            where_clause.append("unaccent(lower(id_registro_combustivel)) LIKE unaccent(lower(:where))")
            parameters["where"] = f"%{where}%"

        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)

        base_query += " LIMIT :limit OFFSET :offset"
        parameters["limit"] = limit
        parameters["offset"] = offset

        result = db.execute(text(base_query), parameters).mappings()

        return [dict(row) for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar registros de combustível: {str(e)}")

def delete_registro_combustivel_by_id(db: Session, id_registro_combustivel: int):
    try:
        result = db.execute(text(
            "DELETE FROM registro_combustivel WHERE id_registro_combustivel = :id_registro_combustivel"
        ), {"id_registro_combustivel": id_registro_combustivel})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar registro de combustível: {str(e)}")