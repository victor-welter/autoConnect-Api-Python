from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.usuario_service import add_user, get_all_users, get_user_by_cpf_cnpj
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/registrar", status_code=201)
async def create_user(user_data: dict, db: Session = Depends(get_db)):
    try:
        new_user = add_user(db, user_data)
        return {"success": True, "data": "Usuário cadastrado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/buscaUsuarios", status_code=200)
async def read_all_users(db: Session = Depends(get_db)):
    try:
        users = get_all_users(db)
        return {"success": True, "data": users}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.post("/login", status_code=200)
async def login_user(cpf_cnpj: str, senha: str, db: Session = Depends(get_db)):
    try:
        user = get_user_by_cpf_cnpj(db, cpf_cnpj)
        if not user:
            return {"success": False, "error": "Usuário não encontrado."}

        if user.senha != senha:
            return {"success": False, "error": "CPF/CNPJ ou senha incorretos."}

        return {"success": True, "data": user}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
