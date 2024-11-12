from src.core.models.pedido_domain import PedidoDomain
from src.presentation.dto.pedido_dto import PedidoDTO

def map_domain_dto_to_pedido(pedidoDTO:PedidoDTO):
    return PedidoDomain(
        fecha=pedidoDTO.fecha,
        estado=pedidoDTO.estado,
        total= pedidoDTO.total,
        idCliente= pedidoDTO.idCliente,
    )