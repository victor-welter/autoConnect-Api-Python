from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.porta_service import add_porta, update_porta, get_portas, delete_porta_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("add_porta/", status_code=201)
async def create_porta(porta_data: dict, db: Session = Depends(get_db)):
    try:
        add_porta(db, porta_data)

        return {"success": True, "data": "Porta cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("update_porta/{id_porta}", status_code=200)
async def update_porta(id_porta: int, porta_data: dict, db: Session = Depends(get_db)):
    try:
        updated = update_porta(db, id_porta, porta_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar a porta.")
        
        return {"success": True, "data": "Porta atualizada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
    
@router.get("/get_portas", status_code=200)
async def read_portas(db: Session = Depends(get_db)):
    try:
        portas = get_portas(db)

        return {"success": True, "data": portas}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_porta/{id_porta}", status_code=200)
async def delete_porta(id_porta: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_porta_by_id(db, id_porta)

        if not deleted:
            raise DatabaseError("Não foi possível deletar a porta.")
        
        return {"success": True, "data": "Porta deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
