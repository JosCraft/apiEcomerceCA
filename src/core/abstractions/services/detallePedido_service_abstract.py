from abc import ABC, abstractmethod

from src.core.models.detallePedido_domain import DetallePedidoDomain
class IDetallePedidoService(ABC):

    @abstractmethod
    async def get_detalle_pedido(self, id_detalle: int) -> DetallePedidoDomain:
        pass

    @abstractmethod
    async def create_detalle_pedido(self, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        pass

    @abstractmethod
    async def update_detalle_pedido(self, id_detalle: int, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        pass

    @abstractmethod
    async def delete_detalle_pedido(self, id_detalle: int) -> None:
        pass

    @abstractmethod
    async def get_all_detalles_pedido(self) -> list[DetallePedidoDomain]:
        pass

