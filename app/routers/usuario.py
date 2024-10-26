from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.usuario_service import add_usuario, update_usuario, get_usuarios, get_usuario_by_email
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_usuario", status_code=201)
async def add_usuario(user_data: dict, db: Session = Depends(get_db)):
    try:
        add_usuario(db, user_data)

        return {"success": True, "data": "Usuário cadastrado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_usuario/{cpf_cnpj}", status_code=200)
async def update_usuario(cpf_cnpj: str, user_data: dict, db: Session = Depends(get_db)):
    try:
        updated = update_usuario(db, cpf_cnpj, user_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o usuário.")

        return {"success": True, "data": "Usuário atualizado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_usuarios", status_code=200)
async def get_usuarios(db: Session = Depends(get_db)):
    try:
        usuarios = get_usuarios(db)

        return {"success": True, "data": usuarios}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_usuario/{email}", status_code=200)
async def get_usuario_by_email(email: str, db: Session = Depends(get_db)):
    try:
        user = get_usuario_by_email(db, email)

        if not user:
            return {"success": False, "error": "Usuário não encontrado."}

        return {"success": True, "data": user}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.post("/login", status_code=200)
async def login(email: str, senha: str, db: Session = Depends(get_db)):
    try:
        user = get_usuario_by_email(db, email)
        if not user:
            return {"success": False, "error": "Usuário não encontrado."}

        if user.senha != senha:
            return {"success": False, "error": "CPF/CNPJ ou senha incorretos."}

        return {"success": True, "data": user}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
