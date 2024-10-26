from .categoria_service import (
    add_categoria,
    update_categoria,
    get_categorias,
    delete_categoria_by_id,
)

from .despesa_service import (
    add_despesa,
    update_despesa,
    get_despesas,
    delete_despesa_by_id,
)

from .local_service import (
    add_local,
    update_local,
    get_locals,
    get_local_by_id,
    delete_local_by_id,
)

from .marca_service import (
    add_marca,
    update_marca,
    get_marcas,
    delete_marca_by_id,
)

from .modelo_service import (
    add_modelo,
    update_modelo,
    get_modelos,
    delete_modelo_by_id,
)

from .permissao_service import (
    add_permissao,
    update_permissao,
    get_permissoes,
    delete_permissao_by_id,
)

from .tipo_combustivel_service import (
    add_tipo_combustivel,
    update_tipo_combustivel,
    get_tipos_combustivel,
    delete_tipo_combustivel_by_id,
)

from .tipo_despesa_service import (
    add_tipo_despesa,
    update_tipo_despesa,
    get_tipos_despesa,
    delete_tipo_despesa_by_id,
)

from .tipo_problema_service import (
    add_tipo_problema,
    update_tipo_problema,
    get_tipos_problema,
    delete_tipo_problema_by_id,
)

from .usuario_permissao_service import (
    add_usuario_permissao,
    delete_usuario_permissao,
)

from .usuario_service import (
    add_usuario,
    update_usuario,
    get_usuarios,
    get_usuario_by_email,
)

from .veiculo_service import (
    add_veiculo,
    update_veiculo,
    get_veiculos,
    delete_veiculo_by_id,
)
