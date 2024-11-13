from abc import ABC, abstractmethod

from src.core.models.delivery_domain import DeliveryDomain


class IDeliveryRepository(ABC):

    @abstractmethod
    async def login(self, email:str, password:str) -> bool:
        pass

