from src.core.models.detallePedido_domain import DetallePedidoDomain
from src.presentation.dto.detallepedido_dto import DetallePedidoDTO


def map_domain_dto_to_detalle_pedido(detallepedidoDTO:DetallePedidoDTO) -> DetallePedidoDomain:
    return DetallePedidoDomain(
        idPedido=detallepedidoDTO.idPedido,
        idProducto=detallepedidoDTO.idProducto,
        cantidad=detallepedidoDTO.cantidad,
        subtotal=detallepedidoDTO.subtotal
    )

