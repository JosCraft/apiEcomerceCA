from src.core.abstractions.infrastructure.repository.detallePedido_repository_abstract import IDetallePedidoRepository
from src.core.abstractions.services.detallePedido_service_abstract import IDetallePedidoService
from src.core.models.detallePedido_domain import DetallePedidoDomain


class DetallePedidoService(IDetallePedidoService):

    def __init__(self, detalle_pedido_repository: IDetallePedidoRepository):
        self.detalle_pedido_repository = detalle_pedido_repository

    async def get_detalle_pedido(self, id_detalle: int) -> DetallePedidoDomain:
        detalle_pedido = await self.detalle_pedido_repository.get(id_detalle)
        if not detalle_pedido:
            raise ValueError(f"Detalle de pedido con ID {id_detalle} no encontrado")
        return detalle_pedido

    async def create_detalle_pedido(self, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        try:
            return await self.detalle_pedido_repository.create(detalle_pedido)
        except Exception as e:
            raise ValueError(f"Error al crear el detalle del pedido: {str(e)}")

    async def update_detalle_pedido(self, id_detalle: int, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        try:
            existing_detalle = await self.detalle_pedido_repository.get(id_detalle)
            if not existing_detalle:
                raise ValueError(f"Detalle de pedido con ID {id_detalle} no encontrado")

            return await self.detalle_pedido_repository.update(id_detalle, detalle_pedido)
        except Exception as e:
            raise ValueError(f"Error al actualizar el detalle del pedido: {str(e)}")

    async def delete_detalle_pedido(self, id_detalle: int) -> None:
        try:
            existing_detalle = await self.detalle_pedido_repository.get(id_detalle)
            if not existing_detalle:
                raise ValueError(f"Detalle de pedido con ID {id_detalle} no encontrado")

            await self.detalle_pedido_repository.delete(id_detalle)
        except Exception as e:
            raise ValueError(f"Error al eliminar el detalle del pedido: {str(e)}")

    async def get_all_detalles_pedido(self) -> list[DetallePedidoDomain]:
        return await self.detalle_pedido_repository.get_all()