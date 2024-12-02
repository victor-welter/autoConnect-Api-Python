from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.registro_porta import RegistroPortaSchema
from app.services.registro_porta_service import add_registro_porta, update_registro_porta, get_registros_porta, delete_registro_porta_by_id
from app.services.email_service import enviar_email 
from app.exceptions import DatabaseError

router = APIRouter()

@router.post("/add_registro_porta", status_code=201)
async def create_registro_porta(registro_porta_data: RegistroPortaSchema, db: Session = Depends(get_db)):
    try:
        if not registro_porta_data.data_hora:
            registro_porta_data.data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        add_registro_porta(db, registro_porta_data)

        destinatarios_email = ["victorwelter2003@gmail.com", "eg0111867@setrem.com.br", "eriquewillers@gmail.com"]

        for destinatario in destinatarios_email:
            enviar_email(
                destinatario_email=destinatario,
                assunto=f"Porta {registro_porta_data.estado_porta}",
                corpo_email=f"A porta foi {registro_porta_data.estado_porta} com sucesso!",
            )

        return {"success": True, "data": "Registro de porta cadastrado com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.put("/update_registro_porta", status_code=200)
async def update_registro_porta(registro_porta_data: RegistroPortaSchema, db: Session = Depends(get_db)):
    try:
        updated = update_registro_porta(db, registro_porta_data)

        if not updated:
            raise DatabaseError("Não foi possível atualizar o registro de porta.")
        
        return {"success": True, "data": "Registro de porta atualizado com sucesso."}
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.get("/get_registros_porta", status_code=200)
async def read_registros_porta(db: Session = Depends(get_db)):
    try:
        registros_porta = get_registros_porta(db)

        return {"success": True, "data": registros_porta}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

@router.delete("/delete_registro_porta", status_code=200)
async def delete_registro_porta(id_registro_porta: int, db: Session = Depends(get_db)):
    try:
        deleted = delete_registro_porta_by_id(db, id_registro_porta)
    
        if not deleted:
            raise DatabaseError("Não foi possível deletar o registro da porta.")
        
        return {"success": True, "data": "Registro da porta deletada com sucesso."}
    
    except DatabaseError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}
