from src.core.abstractions.infrastructure.repository.delivery_repository_abstract import IDeliveryRepository
from src.core.abstractions.services.delivery_service_abstract import IDeliveryService
from src.core.models.delivery_domain import DeliveryDomain

class DeliveryService(IDeliveryService):
    def __init__(self, delivery_repository: IDeliveryRepository):
        self.delivery_repository = delivery_repository

    async def get_delivery(self, idDelivery: int) -> DeliveryDomain:
        print(idDelivery)
        delivery = await self.delivery_repository.get(idDelivery)
        if delivery is None:
            raise ValueError(f"Delivery with id not found")
        return delivery

    async def create_delivery(self, delivery: DeliveryDomain) -> DeliveryDomain:
        try:
            # Ensure that the repository's create method returns the full DeliveryDomain
            last_id = await self.delivery_repository.create(delivery)
            delivery.idDelivery = last_id  # Set the generated ID to the delivery object
            return delivery
        except Exception as e:
            raise ValueError(f"Error creating delivery: {str(e)}")

    async def update_delivery(self, idDelivery: int, delivery: DeliveryDomain) -> DeliveryDomain:
        # Ensure delivery exists first
        existing_delivery = await self.delivery_repository.get(idDelivery)
        if not existing_delivery:
            raise ValueError(f"Delivery with id {idDelivery} not found")

        # Update the delivery and return the updated object
        await self.delivery_repository.update(idDelivery, delivery)
        return await self.delivery_repository.get(idDelivery)

    async def delete_delivery(self, idDelivery: int) -> None:
        # Check if the delivery exists before trying to delete
        existing_delivery = await self.delivery_repository.get(idDelivery)
        if not existing_delivery:
            raise ValueError(f"Delivery with id {idDelivery} not found")

        await self.delivery_repository.delete(idDelivery)

    async def get_all_deliveries(self) -> list[DeliveryDomain]:
        return await self.delivery_repository.get_all()
