from fastapi import APIRouter, Depends, HTTPException, status,Form
from src.core.abstractions.services.delivery_service_abstract import IDeliveryService
from src.core.dependency_inyection.dependency_inyection import build_delivery_service
from src.presentation.dto.delivery_dto import DeliveryDTO
from src.presentation.mappers.map_dto_domain_delivery import map_domain_dto_to_delivery
from src.core.models.delivery_domain import DeliveryDomain

delivery_controller = APIRouter(prefix="/api/v1", tags=["delivery"])

@delivery_controller.get("/deliveries", response_model=list[DeliveryDomain])
async def list_deliveries(
    delivery_service: IDeliveryService = Depends(build_delivery_service)
):
    return await delivery_service.get_all_deliveries()

@delivery_controller.get("/delivery/{id}", response_model=DeliveryDomain)
async def retrieve_delivery(
    id: int,
    delivery_service: IDeliveryService = Depends(build_delivery_service)
):
    delivery = await delivery_service.get_delivery(id)
    if not delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery with ID {id} not found"
        )
    return delivery

@delivery_controller.post("/delivery", response_model=DeliveryDomain, status_code=status.HTTP_201_CREATED)
async def create_delivery(
    delivery_dto: DeliveryDTO,
    delivery_service: IDeliveryService = Depends(build_delivery_service)
):
    delivery = map_domain_dto_to_delivery(delivery_dto)
    return await delivery_service.create_delivery(delivery)
@delivery_controller.post("/login", response_model=DeliveryDomain)
async def login_delivery(
    email: str = Form(...),  # Recibe el correo del delivery desde el formulario
    password: str = Form(...),  # Recibe la contraseña desde el formulario
    delivery_service: IDeliveryService = Depends(build_delivery_service)  # Usando el servicio de delivery
):
    # Verificar si el delivery existe en la base de datos por email
    delivery = await delivery_service.get_delivery_by_email(email)  # Usar el servicio de delivery
    if not delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email no registrado"
        )

    # Verificar si la contraseña coincide
    if delivery.password != password:  # Comparar con la contraseña del delivery
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )

    # Si todo es correcto, devolver el delivery
    return delivery
@delivery_controller.put("/delivery/{id}", response_model=DeliveryDomain)
async def update_delivery(
    id: int,
    delivery_dto: DeliveryDTO,
    delivery_service: IDeliveryService = Depends(build_delivery_service)
):
    existing_delivery = await delivery_service.get_delivery(id)
    if not existing_delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery with ID {id} not found"
        )
    delivery = map_domain_dto_to_delivery(delivery_dto)
    return await delivery_service.update_delivery(id,delivery)

@delivery_controller.delete("/delivery/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery(
    id: int,
    delivery_service: IDeliveryService = Depends(build_delivery_service)
):
    existing_delivery = await delivery_service.get_delivery(id)
    if not existing_delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Delivery with ID {id} not found"
        )
    await delivery_service.delete_delivery(id)
    return {"message": f"Delivery with ID {id} successfully deleted"}
