from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.marca_service import add_marca, update_marca, get_marcas, delete_marca_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("add_marca/", status_code=201)
async def create_marca(marca_data: dict, db: Session = Depends(get_db)):
    try:
        add_marca(db, marca_data)

        return {"success": True, "data": "Marca cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("update_marca/{id_marca}", status_code=200)
async def update_marca_route(id_marca: int, marca_data: dict, db: Session = Depends(get_db)):
    try:
        updated = update_marca(db, id_marca, marca_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar a marca.")
        
        return {"success": True, "data": "Marca atualizada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_marcas", status_code=200)
async def read_marcas(db: Session = Depends(get_db)):
    try:
        marcas = get_marcas(db)

        return {"success": True, "data": marcas}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_marca/{id_marca}", status_code=200)
async def delete_marca(id_marca: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_marca_by_id(db, id_marca)

        if not deleted:
            raise DatabaseError("Não foi possível deletar a marca.")
        
        return {"success": True, "data": "Marca deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}