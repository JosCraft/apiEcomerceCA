from abc import ABC, abstractmethod

from src.core.models.designa_domain import DesignaDomain


class IDesignaRepository(ABC):
    @abstractmethod
    async def create(self, designa: DesignaDomain) -> bool:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass
