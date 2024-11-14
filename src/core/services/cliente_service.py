from src.core.abstractions.infrastructure.repository.cliente_repository_abstract import IClienteRepository
from src.core.abstractions.services.cliente_service_abstract import IClienteService
from src.core.models.cliente_domain import ClienteDomain

class ClienteService(IClienteService):

    def __init__(self, cliente_repository: IClienteRepository):
        self.cliente_repository = cliente_repository

    async def get_cliente(self, idCliente: int) -> ClienteDomain:
        cliente = await self.cliente_repository.get(idCliente)
        if cliente is None:
            raise ValueError(f"Cliente with id {idCliente} not found")
        return cliente

    async def create_cliente(self, cliente: ClienteDomain) -> ClienteDomain:
        try:
            # Create the cliente and return the complete ClienteDomain with ID
            last_id = await self.cliente_repository.create(cliente)
            cliente.idCliente = last_id  # Set the generated ID to the cliente
            return cliente
        except Exception as e:
            raise ValueError(f"Error creating cliente: {str(e)}")

    async def update_cliente(self, idCliente: int, cliente: ClienteDomain) -> ClienteDomain:
        # Ensure cliente exists first
        existing_cliente = await self.cliente_repository.get(idCliente)
        if not existing_cliente:
            raise ValueError(f"Cliente with id {idCliente} not found")

        # Update the cliente and return the updated object
        await self.cliente_repository.update(idCliente, cliente)
        return await self.cliente_repository.get(idCliente)

    async def delete_cliente(self, idCliente: int) -> None:
        # Check if the cliente exists before trying to delete
        existing_cliente = await self.cliente_repository.get(idCliente)
        if not existing_cliente:
            raise ValueError(f"Cliente with id {idCliente} not found")

        await self.cliente_repository.delete(idCliente)

    async def get_all_clientes(self) -> list[ClienteDomain]:
        return await self.cliente_repository.get_all()

    async def get_cliente_by_email(self, email: str) -> ClienteDomain:
        cliente = await self.cliente_repository.get_by_email(email)
        if cliente is None:
            raise ValueError(f"Cliente with email {email} not found")
        return cliente