from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.veiculo import VeiculoSchema
from app.services.veiculo_service import add_veiculo, update_veiculo, get_veiculos, delete_veiculo_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_veiculo", status_code=201)
async def create_veiculo(veiculo_data: VeiculoSchema, db: Session = Depends(get_db)):
    try:
        add_veiculo(db, veiculo_data)

        return {"success": True, "data": "Veículo cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_veiculo", status_code=200)
async def update_veiculo_route(id_veiculo: int, veiculo_data: VeiculoSchema, db: Session = Depends(get_db)):
    try:
        updated = update_veiculo(db, id_veiculo, veiculo_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o veículo.")
        
        return {"success": True, "data": "Veículo atualizado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_veiculos", status_code=200)
async def read_veiculos(db: Session = Depends(get_db)):
    try:
        veiculos = get_veiculos(db)

        return {"success": True, "data": veiculos}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_veiculo", status_code=200)
async def delete_veiculo(id_veiculo: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_veiculo_by_id(db, id_veiculo)

        if not deleted:
            raise DatabaseError("Não foi possível deletar o veículo.")
        
        return {"success": True, "data": "Veículo deletado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}