from src.core.models.delivery_domain import DeliveryDomain
from src.presentation.dto.delivery_dto import DeliveryDTO

def map_domain_dto_to_delivery(deliveryDTO:DeliveryDTO):
    return DeliveryDomain(
        nombre=deliveryDTO.nombre,
        turno=deliveryDTO.turno,
        email=deliveryDTO.email,
        estado=deliveryDTO.estado,
        ubicacion=deliveryDTO.ubicacion,
        password=deliveryDTO.password
    )