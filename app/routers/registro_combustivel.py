from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.registro_combustivel import RegistroCombustivelSchema
from app.services.registro_combustivel_service import add_registro_combustivel, update_registro_combustivel, get_registros_combustivel, delete_registro_combustivel_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_registro_combustivel", status_code=201)
async def create_registro_combustivel(registro_combustivel_data: RegistroCombustivelSchema, db: Session = Depends(get_db)):
    try:
        add_registro_combustivel(db, registro_combustivel_data)

        return {"success": True, "data": "Registro de combustível cadastrado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_registro_combustivel", status_code=200)
async def update_registro_combustivel(registro_combustivel_data: RegistroCombustivelSchema, db: Session = Depends(get_db)):
    try:
        updated = update_registro_combustivel(db, registro_combustivel_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o registro de combustível.")

        return {"success": True, "data": "Registro de combustível atualizado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_registros_combustivel", status_code=200)
async def read_registros_combustivel(db: Session = Depends(get_db)):
    try:
        registros_combustivel = get_registros_combustivel(db)

        return {"success": True, "data": registros_combustivel}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_registro_combustivel", status_code=200)
async def delete_registro_combustivel(id_registro_combustivel: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_registro_combustivel_by_id(db, id_registro_combustivel)

        if not deleted:
            raise DatabaseError("Não foi possível excluir o registro de combustível.")
        
        return {"success": True, "data": "Registro de combustível excluído com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
