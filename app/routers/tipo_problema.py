from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tipo_problema import TipoProblemaSchema
from app.services.tipo_problema_service import add_tipo_problema, update_tipo_problema, get_tipos_problema, delete_tipo_problema_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_tipo_problema", status_code=201)
async def create_tipo_problema(tipo_problema_data: TipoProblemaSchema, db: Session = Depends(get_db)):
    try:
        add_tipo_problema(db, tipo_problema_data)

        return {"success": True, "data": "Tipo de problema cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_tipo_problema", status_code=200)
async def update_tipo_problema_route(id_tipo_problema: int, tipo_problema_data: TipoProblemaSchema, db: Session = Depends(get_db)):
    try:
        updated = update_tipo_problema(db, id_tipo_problema, tipo_problema_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o tipo de problema.")
        
        return {"success": True, "data": "Tipo de problema atualizado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_tipos_problema", status_code=200)
async def read_tipos_problema(db: Session = Depends(get_db)):
    try:
        tipos_problema = get_tipos_problema(db)

        return {"success": True, "data": tipos_problema}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_tipo_problema", status_code=200)
async def delete_tipo_problema(id_tipo_problema: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_tipo_problema_by_id(db, id_tipo_problema)

        if not deleted:
            raise DatabaseError("Não foi possível deletar o tipo de problema.")
        
        return {"success": True, "data": "Tipo de problema deletado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

        
