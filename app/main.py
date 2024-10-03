from fastapi import FastAPI
from app.routers import router 

app = FastAPI()

# Inclui o router das rotas
app.include_router(router)
