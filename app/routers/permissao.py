from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.permissao import PermissaoSchema
from app.services.permissao_service import add_permissao, update_permissao, get_permissoes, delete_permissao_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_permissao", status_code=201)
async def create_permissao(permissao_data: PermissaoSchema, db: Session = Depends(get_db)):
    try:
        add_permissao(db, permissao_data)

        return {"success": True, "data": "Permissão cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_permissao", status_code=200)
async def update_permissao_route(id_permissao: int, permissao_data: PermissaoSchema, db: Session = Depends(get_db)):
    try:
        updated = update_permissao(db, id_permissao, permissao_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar a permissão.")
        
        return {"success": True, "data": "Permissão atualizada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_permissoes", status_code=200)
async def read_permissoes(db: Session = Depends(get_db)):
    try:
        permissoes = get_permissoes(db)

        return {"success": True, "data": permissoes}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_permissao", status_code=200)
async def delete_permissao(id_permissao: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_permissao_by_id(db, id_permissao)

        if not deleted:
            raise DatabaseError("Não foi possível deletar a permissão.")
        
        return {"success": True, "data": "Permissão deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}