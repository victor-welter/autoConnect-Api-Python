import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

def enviar_email(destinatario_email: str, assunto: str, corpo_email: str) -> dict:
    try:
        # Obtém as credenciais do banco de dados a partir das variáveis de ambiente
        REMETENTE_EMAIL = os.getenv("REMETENTE_EMAIL")
        REMETENTE_SENHA = os.getenv("REMETENTE_SENHA")

        # Conecte-se ao servidor SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(REMETENTE_EMAIL, REMETENTE_SENHA)

        # Crie a mensagem de e-mail
        mensagem = MIMEMultipart()
        mensagem['From'] = REMETENTE_EMAIL
        mensagem['To'] = destinatario_email
        mensagem['Subject'] = assunto
        mensagem.attach(MIMEText(corpo_email, 'plain'))

        # Envie o e-mail
        server.sendmail(REMETENTE_EMAIL, destinatario_email, mensagem.as_string())
        server.quit()

        return {"success": True, "message": "E-mail enviado com sucesso!"}

    except smtplib.SMTPAuthenticationError:
        return {"success": False, "error": "Falha na autenticação. Verifique o e-mail e senha."}
    except smtplib.SMTPException as e:
        return {"success": False, "error": f"Erro ao enviar e-mail: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"Erro inesperado: {str(e)}"}
