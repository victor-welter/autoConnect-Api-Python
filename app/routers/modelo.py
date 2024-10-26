from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.modelo_service import add_modelo, update_modelo, get_modelos, delete_modelo_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("add_modelo/", status_code=201)
async def create_modelo(modelo_data: dict, db: Session = Depends(get_db)):
    try:
        add_modelo(db, modelo_data)

        return {"success": True, "data": "Modelo cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("update_modelo/{id_modelo}", status_code=200)
async def update_modelo_route(id_modelo: int, modelo_data: dict, db: Session = Depends(get_db)):
    try:
        updated = update_modelo(db, id_modelo, modelo_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o modelo.")
        
        return {"success": True, "data": "Modelo atualizado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_modelos", status_code=200)
async def read_modelos(db: Session = Depends(get_db)):
    try:
        modelos = get_modelos(db)

        return {"success": True, "data": modelos}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_modelo/{id_modelo}", status_code=200)
async def delete_modelo(id_modelo: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_modelo_by_id(db, id_modelo)

        if not deleted:
            raise DatabaseError("Não foi possível deletar o modelo.")
        
        return {"success": True, "data": "Modelo deletado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}