from abc import ABC, abstractmethod
from src.core.models.delivery_domain import DeliveryDomain


class IDeliveryRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> DeliveryDomain:
        pass

    @abstractmethod
    async def create(self, delivery: DeliveryDomain) -> DeliveryDomain:
        pass

    @abstractmethod
    async def update(self, delivery: DeliveryDomain) -> DeliveryDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    async def get_all(self) -> list[DeliveryDomain]:
        pass

    @abstractmethod
    async def get_delivery_by_email(self, email: str) -> DeliveryDomain:
        pass



