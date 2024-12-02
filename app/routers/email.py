from fastapi import APIRouter, HTTPException
from app.schemas.email import EmailSchema
from app.services.email_service import enviar_email 

router = APIRouter()

@router.post("/enviar_email", status_code=200)
async def enviar_email_api(email: EmailSchema):
    # Envia o e-mail para cada destinatário
    for destinatario in email.destinatarios_email:
        resultado = enviar_email(
            destinatario_email=destinatario,
            assunto=email.assunto,
            corpo_email=email.corpo_email,
        )

        if resultado["success"]:
            return {"success": True, "message": resultado["message"]}
        else:
            raise HTTPException(status_code=400, detail=resultado["error"])
