from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.usuario import UsuarioSchema
from app.services.usuario_service import add_usuario, update_usuario, get_usuarios, get_usuario_by_email
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_usuario", status_code=201)
async def create_usuario(usuario_data: UsuarioSchema, db: Session = Depends(get_db)):
    try:
        add_usuario(db, usuario_data)

        return {"success": True, "data": "Usuário cadastrado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_usuario", status_code=200)
async def update_usuario_by_id(email: str, usuario_data: UsuarioSchema, db: Session = Depends(get_db)):
    try:
        updated = update_usuario(db, email, usuario_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o usuário.")

        return {"success": True, "data": "Usuário atualizado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_usuarios", status_code=200)
async def read_usuarios(where: str = None, limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    try:
        usuarios = get_usuarios(db, where, limit, offset)

        return {"success": True, "data": usuarios}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_usuario", status_code=200)
async def read_usuario_by_email(email: str, db: Session = Depends(get_db)):
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
async def login_usuario(email: str, senha: str, db: Session = Depends(get_db)):
    try:
        print(email, senha)
        users = get_usuario_by_email(db, email)

        if not users:
            return {"success": False, "error": "Usuário não encontrado."}
        
        user = users[0]
        if user["senha"] != senha:
            return {"success": False, "error": "E-mail ou senha incorretos."}
            
        return {"success": True, "data": user}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
