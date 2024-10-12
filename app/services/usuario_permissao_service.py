from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import UsuarioPermissao

def add_usuario_permissao(db: Session, usuario_permissao: UsuarioPermissao):
    try:
        db.execute(text(
            "INSERT INTO usuario_permissao (id_usuario, id_permissao)"
            "VALUES (:id_usuario, :id_permissao)"
        ), {
            "id_usuario": usuario_permissao.id_usuario,
            "id_permissao": usuario_permissao.id_permissao
        })
        db.commit()  
    except Exception as e:
        raise DatabaseError(f"Erro ao salvar permissão de usuário: {str(e)}")

def delete_usuario_permissao(db: Session, id_usuario: int, id_permissao: int):
    try:
        result = db.execute(text(
            "DELETE FROM usuario_permissao "
            "WHERE id_usuario = :id_usuario AND id_permissao = :id_permissao"
        ), {
            "id_usuario": id_usuario,
            "id_permissao": id_permissao
        })
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Erro ao excluir permissão de usuário: {str(e)}")