from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.usuario_permissao import UsuarioPermissaoSchema
from app.services.usuario_permissao_service import add_usuario_permissao, delete_usuario_permissao
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_usuario_permissao", status_code=201)
async def create_usuario_permissao(usuario_permissao_data: UsuarioPermissaoSchema, db: Session = Depends(get_db)):
    try:
        add_usuario_permissao(db, usuario_permissao_data)

        return {"success": True, "data": "Permissão do usuário cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_usuario_permissao", status_code=200)
async def delete_usuario_permissao(id_usuario_permissao: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_usuario_permissao(db, id_usuario_permissao)

        if not deleted:
            raise DatabaseError("Não foi possível deletar a permissão do usuário.")
        
        return {"success": True, "data": "Permissão do usuário deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}