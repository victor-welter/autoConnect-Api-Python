from sqlalchemy.orm import Session
from sqlalchemy import text
from app.exceptions import DatabaseError
from app.models import Usuario

def add_usuario(db: Session, usuario: Usuario):
    try:
        db.execute(text(
            "INSERT INTO usuario (nome, email, senha)"
            "VALUES (:nome, :email, :senha)"
        ), {
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": usuario.senha
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar usuário: {str(e)}")

def update_usuario(db: Session, id_usuario: int, usuario: Usuario):
    try:
        result = db.execute(text(
            "UPDATE usuario "
            "SET nome = :nome, email = :email, senha = :senha "
            "WHERE id_usuario = :id_usuario"
        ), {
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": usuario.senha,
            "id_usuario": id_usuario
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao atualizar usuário: {str(e)}")

def get_usuarios(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_usuario, 
                nome,
                email,
                senha
            FROM usuario 
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
        raise DatabaseError(f"Erro ao buscar usuários: {str(e)}")

def get_usuario_by_email(db: Session, email: str):
    try:
        result = db.execute(text(
            "SELECT "
            "id_usuario, "
            "nome, "
            "email, "
            "senha "
            "FROM usuario "
            "WHERE email = :email"
        ), {
            "email": email
        })
        return result.fetchone()
    except Exception as e:
        raise DatabaseError(f"Erro ao buscar usuário por e-mail: {str(e)}")

def delete_usuario(db: Session, id_usuario: int):
    try:
        result = db.execute(text(
            "DELETE FROM usuario "
            "WHERE id_usuario = :id_usuario"
        ), {
            "id_usuario": id_usuario
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao deletar usuário: {str(e)}")