from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.categoria import CategoriaSchema
from app.services.categoria_service import add_categoria, update_categoria, get_categorias, delete_categoria_by_id
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_categoria", status_code=201)
async def create_categoria(categoria_data: CategoriaSchema, db: Session = Depends(get_db)):
    try:
        add_categoria(db, categoria_data)

        return {"success": True, "data": "Categoria cadastrada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_categoria", status_code=200)
async def update_categoria_route(id_categoria: int, categoria_data: CategoriaSchema, db: Session = Depends(get_db)):
    try:
        updated = update_categoria(db, id_categoria, categoria_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar a categoria.")
        
        return {"success": True, "data": "Categoria atualizada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
    
@router.get("/get_categorias", status_code=200)
async def read_categorias(db: Session = Depends(get_db)):
    try:
        categorias = get_categorias(db)

        return {"success": True, "data": categorias}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_categoria", status_code=200)
async def delete_categoria(id_categoria: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_categoria_by_id(db, id_categoria)

        if not deleted:
            raise DatabaseError("Não foi possível deletar a categoria.")
        
        return {"success": True, "data": "Categoria deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}