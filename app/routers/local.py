from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.local_service import add_local, update_local, get_locals, get_local_by_id, delete_local_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_local", status_code=201)
async def create_local(local_data: dict, db: Session = Depends(get_db)):
    try:
        add_local(db, local_data)

        return {"success": True, "data": "Local cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

    
@router.put("/update_local/{id_local}", status_code=200)
async def update_local_route(id_local: int, local_data: dict, db: Session = Depends(get_db)):
    try:
        updated = update_local(db, id_local, local_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o local.")
        
        return {"success": True, "data": "Local atualizado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/get_locals", status_code=200)
async def read_locais(db: Session = Depends(get_db)):
    try:
        locais = get_locals(db)

        return {"success": True, "data": locais}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/get_local/{id_local}", status_code=200)
async def read_local(id_local: int, db: Session = Depends(get_db)):
    try:
        local = get_local_by_id(db, id_local)

        return {"success": True, "data": local}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
