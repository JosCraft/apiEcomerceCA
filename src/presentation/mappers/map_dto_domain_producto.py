from src.core.models.producto_domain import ProductoDomain
from src.presentation.dto.producto_dto import ProductoDTO
def map_domain_dto_to_producto(productoDTO:ProductoDTO)->ProductoDomain:
    return ProductoDomain (
        nombre =productoDTO.nombre,
        descripcion=productoDTO.descripcion,
        precio=productoDTO.precio,
        descuento=productoDTO.descuento,
        imagen=productoDTO.imagen,
        stock=productoDTO.stock,
        idCategoria=productoDTO.idCategoria
    )
