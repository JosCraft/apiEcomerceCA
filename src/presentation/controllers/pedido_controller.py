from fastapi import APIRouter, Depends, HTTPException, status
from src.core.abstractions.services.pedido_service_abstract import IPedidoService
from src.core.dependency_inyection.dependency_inyection import build_pedido_service
from src.presentation.dto.pedido_dto import PedidoDTO
from src.presentation.mappers.map_dto_domain_pedido import map_domain_dto_to_pedido
from src.core.models.pedido_domain import PedidoDomain

pedido_controller = APIRouter(prefix="/api/v1", tags=["pedido"])

@pedido_controller.get("/pedidos", response_model=list[PedidoDomain])
async def list_pedidos(
    pedido_service: IPedidoService = Depends(build_pedido_service)
):
    return await pedido_service.get_all_pedidos()

@pedido_controller.get("/pedido/{id}", response_model=PedidoDomain)
async def retrieve_pedido(
    id: int,
    pedido_service: IPedidoService = Depends(build_pedido_service)
):
    pedido = await pedido_service.get_pedido(id)
    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido with ID {id} not found"
        )
    return pedido

@pedido_controller.post("/pedido", response_model=PedidoDomain, status_code=status.HTTP_201_CREATED)
async def create_pedido(
    pedido_dto: PedidoDTO,
    pedido_service: IPedidoService = Depends(build_pedido_service)
):
    pedido = map_domain_dto_to_pedido(pedido_dto)
    return await pedido_service.create_pedido(pedido)

@pedido_controller.put("/pedido/{id}", response_model=PedidoDomain)
async def update_pedido(
    id: int,
    pedido_dto: PedidoDTO,
    pedido_service: IPedidoService = Depends(build_pedido_service)
):
    existing_pedido = await pedido_service.get_pedido(id)
    if not existing_pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido with ID {id} not found"
        )
    pedido = map_domain_dto_to_pedido(pedido_dto)
    return await pedido_service.update_pedido(id,pedido)

@pedido_controller.delete("/pedido/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pedido(
    id: int,
    pedido_service: IPedidoService = Depends(build_pedido_service)
):
    existing_pedido = await pedido_service.get_pedido(id)
    if not existing_pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido with ID {id} not found"
        )
    await pedido_service.delete_pedido(id)
