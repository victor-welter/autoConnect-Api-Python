from sqlalchemy.orm import Session
from sqlalchemy import text
from app.exceptions import DatabaseError
from app.models import User  # Ajuste para o seu modelo de usuário

def add_user(db: Session, user_data: dict):
    try:
        new_user = User(**user_data)  # Supondo que você tenha um modelo User definido
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise DatabaseError(f"Erro ao adicionar usuário: {str(e)}")

def get_all_users(db: Session):
    try:
        result = db.execute(text("SELECT * FROM usuario")).fetchall()
        return result
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar usuários: {str(e)}")

def get_user_by_cpf_cnpj(db: Session, cpf_cnpj: str):
    try:
        result = db.execute(text(
            "SELECT * FROM usuario WHERE cpf_cnpj = :cpf_cnpj"
        ), {"cpf_cnpj": cpf_cnpj}).fetchone()
        return result
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar usuário: {str(e)}")
