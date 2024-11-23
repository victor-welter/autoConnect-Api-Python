from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.porta import PortaSchema
from app.services.porta_service import add_porta, update_porta, get_portas, get_porta_by_id, delete_porta_by_id
from app.exceptions import DatabaseError
from datetime import datetime

router = APIRouter()

@router.get("/hora_atual", response_model=str)
def hora_atual():
    # Obtém a hora atual e retorna
    hora = datetime.now().strftime("%H:%M:%S")
    return hora

@router.post("/add_porta", status_code=201)
async def create_porta(porta_data: PortaSchema, db: Session = Depends(get_db)):
    try:
        add_porta(db, porta_data)

        return {"success": True, "data": "Porta cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_porta", status_code=200)
def update_porta(porta_data: PortaSchema, db: Session = Depends(get_db)):
    try:
        print(f"Dados recebidos: {porta_data}") 

        updated = update_porta(db, porta_data)

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

@router.get("/get_porta", status_code=200)
async def read_porta_by_id(id_porta: int, db: Session = Depends(get_db)):
    try:
        porta = get_porta_by_id(db, id_porta)
    
        if not porta:
            raise DatabaseError("Porta não encontrada.")
        
        return {"success": True, "data": porta}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_porta", status_code=200)
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
