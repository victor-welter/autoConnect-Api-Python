from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Veiculo

def add_veiculo(db: Session, veiculo: Veiculo):
    try:
        db.execute(text(
            "INSERT INTO veiculo (placa, ano, odometro, capacidade_tanque, voltagem_min, voltagem_max, id_marca, id_modelo, id_usuario)"
            "VALUES (:placa, :ano, :odometro, :capacidade_tanque, :voltagem_min, :voltagem_max, :id_marca, :id_modelo, :id_usuario)"
        ), {
            "placa": veiculo.placa,
            "ano": veiculo.ano,
            "cor": veiculo.cor,
            "odometro": veiculo.odometro,
            "capacidade_tanque": veiculo.capacidade_tanque,
            "voltagem_min": veiculo.voltagem_min,
            "voltagem_max": veiculo.voltagem_max,
            "id_marca": veiculo.id_marca,
            "id_modelo": veiculo.id_modelo,
            "id_usuario": veiculo.id_usuario
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar veículo: {str(e)}")

def update_veiculo(db: Session, id_veiculo: int, veiculo: Veiculo):
    try:
        result = db.execute(text(
            "UPDATE veiculo "
            "SET placa = :placa, ano = :ano, cor = :cor, odometro = :odometro, capacidade_tanque = :capacidade_tanque, voltagem_min = :voltagem_min, voltagem_max = :voltagem_max, id_marca = :id_marca, id_modelo = :id_modelo, id_usuario = :id_usuario "
            "WHERE id_veiculo = :id_veiculo"
        ), {
            "placa": veiculo.placa,
            "ano": veiculo.ano,
            "cor": veiculo.cor,
            "odometro": veiculo.odometro,
            "capacidade_tanque": veiculo.capacidade_tanque,
            "voltagem_min": veiculo.voltagem_min,
            "voltagem_max": veiculo.voltagem_max,
            "id_marca": veiculo.id_marca,
            "id_modelo": veiculo.id_modelo,
            "id_usuario": veiculo.id_usuario,
            "id_veiculo": id_veiculo
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar veículo: {str(e)}")

def get_veiculos(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_veiculo, 
                placa,
                ano,
                cor,
                odometro,
                capacidade_tanque,
                voltagem_min,
                voltagem_max,
                id_marca,
                id_modelo,
                id_usuario
            FROM veiculo 
        """

        where_clause = []
        parameters = {}

        if where:
            where_clause.append("unaccent(lower(placa)) LIKE unaccent(lower(:where))")
            parameters["where"] = f"%{where}%"

        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)
        
        base_query += " LIMIT :limit OFFSET :offset"
        parameters["limit"] = limit
        parameters["offset"] = offset

        result = db.execute(text(base_query), parameters).mappings()

        return [dict(row) for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar veículos: {str(e)}")
    
def get_veiculo(db: Session, id_veiculo: int):
    try:
        base_query = """
            SELECT 
                id_veiculo, 
                placa,
                ano,
                cor,
                odometro,
                capacidade_tanque,
                voltagem_min,
                voltagem_max,
                id_marca,
                id_modelo,
                id_usuario
            FROM veiculo 
        """

        where_clause = []
        parameters = {}

        where_clause.append("id_veiculo = :id_veiculo")
        parameters["id_veiculo"] = f"{id_veiculo}"
        base_query += " WHERE " + " AND ".join(where_clause)

        result = db.execute(text(base_query), parameters).mappings()

        return [dict(row) for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar veículos: {str(e)}")

def delete_veiculo_by_id(db: Session, id_veiculo: int):
    try:
        result = db.execute(text(
            "DELETE FROM veiculo WHERE id_veiculo = :id_veiculo"
        ), {"id_veiculo": id_veiculo})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar veículo: {str(e)}")