from fastapi import Depends


from src.core.services.cliente_service import ClienteService
from src.core.services.producto_service import ProductoService
from src.core.services.delivery_service import DeliveryService
from src.core.services.pedido_service import PedidoService
from src.core.services.detallePedido_service import DetallePedidoService
from src.core.services.categoria_service import CategoriaService


from src.infrastructure.repository.dependency_inyection.dependency_inyection import get_db_connection

from src.infrastructure.repository.implementations.cliente_repository import ClienteRepository
from src.infrastructure.repository.implementations.producto_repository import ProductoRepository
from src.infrastructure.repository.implementations.delivery_repository import deliveryRepository
from src.infrastructure.repository.implementations.pedido_repository import PedidoRepository
from src.infrastructure.repository.implementations.detallePedido_repository import DetallePedidoRepository
from src.infrastructure.repository.implementations.categoria_repository import CategoriaRepository


def build_cliente_service(
        db_connection=Depends(get_db_connection)
):
    return ClienteService(ClienteRepository(db_connection))


def build_prodcuto_service(
        db_connection=Depends(get_db_connection)
):
    return ProductoService(ProductoRepository(db_connection))


def build_delivery_service(
        db_connection=Depends(get_db_connection)
):
    return DeliveryService(deliveryRepository(db_connection))


def build_pedido_service(
        db_connection=Depends(get_db_connection)
):
    return PedidoService(PedidoRepository(db_connection))


def build_detalle_pedido_service(
        db_connection=Depends(get_db_connection)
):
    return DetallePedidoService(DetallePedidoRepository(db_connection))


def build_categoria_service(
    db_connection = Depends(get_db_connection)
):
    return CategoriaService(CategoriaRepository(db_connection))

