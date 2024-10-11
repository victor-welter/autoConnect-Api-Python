from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Veiculo

def add_veiculo(db: Session, veiculo: Veiculo):
    try:
        db.execute(text(
            "INSERT INTO veiculo (placa, id_marca, id_modelo, ano, cor, id_usuario)"
            "VALUES (:placa, :id_marca, :id_modelo, :ano, :cor, :id_usuario)"
        ), {
            "placa": veiculo.placa,
            "id_marca": veiculo.id_marca,
            "id_modelo": veiculo.id_modelo,
            "ano": veiculo.ano,
            "cor": veiculo.cor,
            "id_usuario": veiculo.id_usuario
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar veículo: {str(e)}")

# TODO - Implementar atualização de veículos
def update_veiculo(db: Session, id_veiculo: int, veiculo: Veiculo):
    try:
        print("Teste")
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar veículo: {str(e)}")

# TODO - Implementar busca de veículos
def get_veiculos(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        print("Teste")
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