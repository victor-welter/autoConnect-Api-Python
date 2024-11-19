from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.marca_service import add_marca, update_marca, get_marcas, delete_marca_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("send_email/", status_code=201)
async def create_marca(marca_data: dict, db: Session = Depends(get_db)):
    try:
        add_marca(db, marca_data)

        return {"success": True, "data": "Marca cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
