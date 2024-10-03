from fastapi import APIRouter
from .local import router as local_router 

router = APIRouter()

# Inclui o router das rotas de local
router.include_router(local_router, prefix="/local", tags=["local"])
