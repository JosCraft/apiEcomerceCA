from fastapi import APIRouter, Depends, HTTPException, status
from src.core.abstractions.services.detallePedido_service_abstract import IDetallePedidoService
from src.core.dependency_inyection.dependency_inyection import build_detalle_pedido_service
from src.presentation.dto.detallepedido_dto import DetallePedidoDTO
from src.presentation.mappers.map_dto_domain_detallepedido import map_domain_dto_to_detalle_pedido
from src.core.models.detallePedido_domain import DetallePedidoDomain

detalle_pedido_controller = APIRouter(prefix="/api/v1", tags=["detalle_pedido"])

@detalle_pedido_controller.get("/detalles_pedido", response_model=list[DetallePedidoDomain])
async def list_detalles_pedido(
    detalle_pedido_service: IDetallePedidoService = Depends(build_detalle_pedido_service)
):
    return await detalle_pedido_service.get_all_detalles_pedido()

@detalle_pedido_controller.get("/detalle_pedido/{id}", response_model=DetallePedidoDomain)
async def retrieve_detalle_pedido(
    id: int,
    detalle_pedido_service: IDetallePedidoService = Depends(build_detalle_pedido_service)
):
    detalle_pedido = await detalle_pedido_service.get_detalle_pedido(id)
    if not detalle_pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"DetallePedido with ID {id} not found"
        )
    return detalle_pedido

@detalle_pedido_controller.post("/detalle_pedido", response_model=DetallePedidoDomain, status_code=status.HTTP_201_CREATED)
async def create_detalle_pedido(
    detalle_pedido_dto: DetallePedidoDTO,
    detalle_pedido_service: IDetallePedidoService = Depends(build_detalle_pedido_service)
):
    detalle_pedido = map_domain_dto_to_detalle_pedido(detalle_pedido_dto)
    return await detalle_pedido_service.create_detalle_pedido(detalle_pedido)

@detalle_pedido_controller.put("/detalle_pedido/{id}", response_model=DetallePedidoDomain)
async def update_detalle_pedido(
    id: int,
    detalle_pedido_dto: DetallePedidoDTO,
    detalle_pedido_service: IDetallePedidoService = Depends(build_detalle_pedido_service)
):
    existing_detalle_pedido = await detalle_pedido_service.get_detalle_pedido(id)
    if not existing_detalle_pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"DetallePedido with ID {id} not found"
        )
    detalle_pedido = map_domain_dto_to_detalle_pedido(detalle_pedido_dto)
    return await detalle_pedido_service.update_detalle_pedido(id, detalle_pedido)

@detalle_pedido_controller.delete("/detalle_pedido/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_detalle_pedido(
    id: int,
    detalle_pedido_service: IDetallePedidoService = Depends(build_detalle_pedido_service)
):
    existing_detalle_pedido = await detalle_pedido_service.get_detalle_pedido(id)
    if not existing_detalle_pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"DetallePedido with ID {id} not found"
        )
    await detalle_pedido_service.delete_detalle_pedido(id)
