from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.tipo_despesa_service import add_tipo_despesa, update_tipo_despesa, get_tipos_despesa, delete_tipo_despesa_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("add_tipo_despesa/", status_code=201)
async def create_tipo_despesa(tipo_despesa_data: dict, db: Session = Depends(get_db)):
    try:
        add_tipo_despesa(db, tipo_despesa_data)

        return {"success": True, "data": "Tipo de despesa cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("update_tipo_despesa/{id_tipo_despesa}", status_code=200)
async def update_tipo_despesa_route(id_tipo_despesa: int, tipo_despesa_data: dict, db: Session = Depends(get_db)):  
    try:
        updated = update_tipo_despesa(db, id_tipo_despesa, tipo_despesa_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o tipo de despesa.")
        
        return {"success": True, "data": "Tipo de despesa atualizado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_tipos_despesa", status_code=200)
async def read_tipos_despesa(db: Session = Depends(get_db)):
    try:
        tipos_despesa = get_tipos_despesa(db)

        return {"success": True, "data": tipos_despesa}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}