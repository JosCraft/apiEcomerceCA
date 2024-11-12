from src.core.models.cliente_domain import ClienteDomain
from src.presentation.dto.cliente_dto import clienteDTO


def map_domain_dto_to_cliente(clienteDTO:clienteDTO) -> ClienteDomain:
    return ClienteDomain(
        nombre=clienteDTO.nombre,
        direccion=clienteDTO.direccion,
        telefono=clienteDTO.telefono,
        email=clienteDTO.email,
        password=clienteDTO.password
    )
