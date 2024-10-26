from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.tipo_combustivel_service import add_tipo_combustivel, update_tipo_combustivel, get_tipos_combustivel, delete_tipo_combustivel_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("add_tipo_combustivel/", status_code=201)
async def create_tipo_combustivel(tipo_combustivel_data: dict, db: Session = Depends(get_db)):
    try:
        add_tipo_combustivel(db, tipo_combustivel_data)

        return {"success": True, "data": "Tipo de combustível cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("update_tipo_combustivel/{id_tipo_combustivel}", status_code=200)
async def update_tipo_combustivel_route(id_tipo_combustivel: int, tipo_combustivel_data: dict, db: Session = Depends(get_db)):
    try:
        updated = update_tipo_combustivel(db, id_tipo_combustivel, tipo_combustivel_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o tipo de combustível.")
        
        return {"success": True, "data": "Tipo de combustível atualizado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_tipos_combustivel", status_code=200)
async def read_tipos_combustivel(db: Session = Depends(get_db)):
    try:
        tipos_combustivel = get_tipos_combustivel(db)

        return {"success": True, "data": tipos_combustivel}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
    
@router.delete("/delete_tipo_combustivel/{id_tipo_combustivel}", status_code=200)
async def delete_tipo_combustivel(id_tipo_combustivel: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_tipo_combustivel_by_id(db, id_tipo_combustivel)

        if not deleted:
            raise DatabaseError("Não foi possível deletar o tipo de combustível.")
        
        return {"success": True, "data": "Tipo de combustível deletado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}