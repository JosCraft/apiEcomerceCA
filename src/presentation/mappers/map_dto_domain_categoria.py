from src.core.models.categoria_domain import CategoriaDomain
from src.presentation.dto.categoria_dto import CategoriaDTO
def map_domain_dto_to_categoria(categoriaDTO:CategoriaDTO)->CategoriaDomain:
    return CategoriaDomain (
        nombre =categoriaDTO.nombreCategoria
    )