from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Despesa

def add_despesa(db: Session, despesa: Despesa):
    try:
        db.execute(text(
            "INSERT INTO despesa (id_tipo_despesa, id_marca, descricao, valor, data) "
            "VALUES (:id_tipo_despesa, :id_marca, :descricao, :valor, :data)"
        ), {
            "id_tipo_despesa": despesa.id_tipo_despesa,
            "id_marca": despesa.id_marca,
            "descricao": despesa.descricao,
            "valor": despesa.valor,
            "data": despesa.data,
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar despesa: {str(e)}")

def update_despesa(db: Session, id_despesa: int, despesa: Despesa):
    try:
        result = db.execute(text(
            "UPDATE despesa "
            "SET id_tipo_despesa = :id_tipo_despesa, id_marca = :id_marca, descricao = :descricao, valor = :valor, data = :data "
            "WHERE id_despesa = :id_despesa"
        ), {
            "id_tipo_despesa": despesa.id_tipo_despesa,
            "id_marca": despesa.id_marca,
            "descricao": despesa.descricao,
            "valor": despesa.valor,
            "data": despesa.data,
            "id_despesa": id_despesa
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar despesa: {str(e)}")

def get_despesas(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_despesa, 
                id_tipo_despesa,
                id_marca,
                descricao,
                valor,
                data
            FROM despesa 
        """

        where_clause = []
        parameters = {}

        if where:
            where_clause.append(where)
        
        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)

        base_query += f" LIMIT {limit} OFFSET {offset}"

        result = db.execute(text(base_query), parameters)

        return result.fetchall()
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar despesas: {str(e)}")

def delete_despesa_by_id(db: Session, id_despesa: int):
    try:
        result = db.execute(text(
            "DELETE FROM despesa WHERE id_despesa = :id_despesa"
        ), {"id_despesa": id_despesa})
        db.commit()
        return result.rowcount > 0 
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar despesa: {str(e)}")