from fastapi import Depends

from src.core.services.example_service import ExampleService
from src.core.services.cliente_service import ClienteService
from src.core.services.producto_service import ProductoService
from src.core.services.delivery_service import DeliveryService
from src.core.services.pedido_service import PedidoService
from src.core.services.detallePedido_service import DetallePedidoService


from src.infrastructure.repository.dependency_inyection.dependency_inyection import get_db_connection

from src.infrastructure.repository.implementations.example_repository import ExampleRepository
from src.infrastructure.repository.implementations.cliente_repository import ClienteRepository
from src.infrastructure.repository.implementations.producto_repository import ProductoRepository
from src.infrastructure.repository.implementations.delivery_repository import DeliveryRepository
from src.infrastructure.repository.implementations.pedido_repository import PedidoRepository
from src.infrastructure.repository.implementations.detallePedido_repository import DetallePedidoRepository



def build_example_service(
        db_connection=Depends(get_db_connection)
):
    return ExampleService(ExampleRepository(db_connection))


def build_cliente_service(
        db_connection=Depends(get_db_connection)
):
    return ClienteService(ClienteRepository(db_connection))

def build_producto_service(
        db_connection=Depends(get_db_connection)
):
    return ProductoService(ProductoRepository(db_connection))

def build_delivery_service(
        db_connection=Depends(get_db_connection)
):
    return DeliveryService(DeliveryRepository(db_connection))


def build_pedido_service(
        db_connection=Depends(get_db_connection)
):
    return PedidoService(PedidoRepository(db_connection))

def build_detallePedido_service(
        db_connection=Depends(get_db_connection)
):
    return DetallePedidoService(DetallePedidoRepository(db_connection))



