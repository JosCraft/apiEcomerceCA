from abc import ABC, abstractmethod

from src.core.models.delivery_domain import DeliveryDomain


class IDeliveryService(ABC):

    @abstractmethod
    async def get_delivery(self, idDelivery: int) -> DeliveryDomain:
        pass

    @abstractmethod
    async def create_delivery(self, delivery: DeliveryDomain) -> DeliveryDomain:
        pass

    @abstractmethod
    async def update_delivery(self, delivery: DeliveryDomain) -> DeliveryDomain:
        pass

    @abstractmethod
    async def delete_delivery(self, idDelivery: int) -> None:
        pass

    @abstractmethod
    async def get_all_deliveries(self) -> list[DeliveryDomain]:
        pass