from fastapi import APIRouter, Depends, HTTPException, status
from src.core.abstractions.services.cliente_service_abstract import IClienteService
from src.core.dependency_inyection.dependency_inyection import build_cliente_service
from src.presentation.dto.cliente_dto import clienteDTO
from src.presentation.mappers.map_dto_domain_cliente import map_domain_dto_to_cliente
from src.core.models.cliente_domain import ClienteDomain

cliente_controller = APIRouter(prefix="/api/v1", tags=["cliente"])


@cliente_controller.get("/cliente", response_model=list[ClienteDomain])
async def list_clientes(
    cliente_service: IClienteService = Depends(build_cliente_service)
):
    return await cliente_service.get_all_clientes()


@cliente_controller.get("/cliente/{id}", response_model=ClienteDomain)
async def retrieve_cliente(
    id: int,
    cliente_service: IClienteService = Depends(build_cliente_service)
):
    cliente = await cliente_service.get_cliente(id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente with ID {id} not found"
        )
    return cliente


@cliente_controller.post("/cliente", response_model=ClienteDomain, status_code=status.HTTP_201_CREATED)
async def create_cliente(
    cliente_dto: clienteDTO,
    cliente_service: IClienteService = Depends(build_cliente_service)
):
    print('dt')
    print(cliente_dto)
    cliente = map_domain_dto_to_cliente(cliente_dto)
    print('mp')
    print(cliente)
    return await cliente_service.create_cliente(cliente)


@cliente_controller.put("/cliente/{id}", response_model=ClienteDomain)
async def update_cliente(
    id: int,
    cliente_dto: clienteDTO,
    cliente_service: IClienteService = Depends(build_cliente_service)
):
    existing_cliente = await cliente_service.get_cliente(id)
    if not existing_cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente with ID {id} not found"
        )
    cliente = map_domain_dto_to_cliente(cliente_dto)
    return await cliente_service.update_cliente(id, cliente)


@cliente_controller.delete("/cliente/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente(
    id: int,
    cliente_service: IClienteService = Depends(build_cliente_service)
):
    existing_cliente = await cliente_service.get_cliente(id)
    if not existing_cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente with ID {id} not found"
        )
    await cliente_service.delete_cliente(id)
    return {"message": f"Cliente with ID {id} successfully deleted"}
