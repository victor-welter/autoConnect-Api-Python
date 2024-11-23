from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.despesa import DespesaSchema
from app.services.despesa_service import add_despesa, update_despesa, get_despesas, delete_despesa_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_despesa", status_code=201)
async def create_despesa(despesa_data: DespesaSchema, db: Session = Depends(get_db)):
    try:
        add_despesa(db, despesa_data)

        return {"success": True, "data": "Despesa cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_despesa", status_code=200)
async def update_despesa_route(id_despesa: int, despesa_data: DespesaSchema, db: Session = Depends(get_db)):
    try:
        updated = update_despesa(db, id_despesa, despesa_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar a despesa.")
        
        return {"success": True, "data": "Despesa atualizada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_despesas", status_code=200)
async def read_despesas(db: Session = Depends(get_db)):
    try:
        despesas = get_despesas(db)

        return {"success": True, "data": despesas}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
    
@router.delete("/delete_despesa", status_code=200)
async def delete_despesa(id_despesa: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_despesa_by_id(db, id_despesa)

        if not deleted:
            raise DatabaseError("Não foi possível deletar a despesa.")
        
        return {"success": True, "data": "Despesa deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}