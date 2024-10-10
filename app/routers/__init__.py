from fastapi import APIRouter
from .categoria import router as categoria_router
from .despesa import router as despesa_router
from .local import router as local_router
from .marca import router as marca_router
from .modelo import router as modelo_router
from .permissao import router as permissao_router
from .tipo_combustivel import router as tipo_combustivel_router
from .tipo_despesa import router as tipo_despesa_router
from .tipo_problema import router as tipo_problema_router
from .usuario_permissao import router as usuario_permissao_router
from .usuario import router as usuario_router
from .veiculo import router as veiculo_router

router = APIRouter()

# Inclui o router das rotas de local
router.include_router(categoria_router, prefix="/categoria", tags=["categoria"])
router.include_router(despesa_router, prefix="/despesa", tags=["despesa"])
router.include_router(local_router, prefix="/local", tags=["local"])
router.include_router(marca_router, prefix="/marca", tags=["marca"])
router.include_router(modelo_router, prefix="/modelo", tags=["modelo"])
router.include_router(permissao_router, prefix="/permissao", tags=["permissao"])
router.include_router(tipo_combustivel_router, prefix="/tipo_combustivel", tags=["tipo_combustivel"])
router.include_router(tipo_despesa_router, prefix="/tipo_despesa", tags=["tipo_despesa"])
router.include_router(tipo_problema_router, prefix="/tipo_problema", tags=["tipo_problema"])
router.include_router(usuario_permissao_router, prefix="/usuario_permissao", tags=["usuario_permissao"])
router.include_router(usuario_router, prefix="/usuario", tags=["usuario"])
router.include_router(veiculo_router, prefix="/veiculo", tags=["veiculo"])
