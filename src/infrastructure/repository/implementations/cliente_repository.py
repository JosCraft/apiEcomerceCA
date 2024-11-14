from src.core.abstractions.infrastructure.repository.cliente_repository_abstract import IClienteRepository
from src.core.models.cliente_domain import ClienteDomain

class ClienteRepository(IClienteRepository):

    def __init__(self, connection: object) -> object:
        self.connection = connection

    async def get(self, id: int) -> ClienteDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM cliente WHERE idCliente=%s", (id,))
                result = cursor.fetchone()
                if result:
                    return ClienteDomain(
                        idCliente=result['idCliente'],
                        nombre=result['nombre'],
                        direccion=result['direccion'],
                        telefono=result['telefono'],
                        email=result['email'],
                        password=result['password']
                    )
        except Exception as error:
            print(f"Error en 'get': {error}")
        return None

    async def get_by_email(self, email: str) -> ClienteDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM cliente WHERE email=%s", (email,))
                result = cursor.fetchone()
                if result:
                    return ClienteDomain(
                        idCliente=result['idCliente'],
                        nombre=result['nombre'],
                        direccion=result['direccion'],
                        telefono=result['telefono'],
                        email=result['email'],
                        password=result['password']
                    )
        except Exception as error:
            print(f"Error en 'get_by_email': {error}")
        return None
    async def create(self, cliente: ClienteDomain) -> int:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO cliente (nombre, direccion, telefono, email, password)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        cliente.nombre,
                        cliente.direccion,
                        cliente.telefono,
                        cliente.email,
                        cliente.password
                    )
                )
                self.connection.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]
                return last_id
        except Exception as err:
            print(f"Error en 'create': {err}")
            return None

    async def update(self, idCliente: int, cliente: ClienteDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE cliente 
                    SET nombre=%s, direccion=%s, telefono=%s, email=%s, password=%s
                    WHERE idCliente=%s
                    """,
                    (
                        cliente.nombre,
                        cliente.direccion,
                        cliente.telefono,
                        cliente.email,
                        cliente.password,
                        idCliente
                    )
                )
                self.connection.commit()
                return True
        except Exception as err:
            print(f"Error en 'update': {err}")
            return False

    async def delete(self, id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM cliente WHERE idCliente=%s", (id,))
                self.connection.commit()
                return True
        except Exception as err:
            print(f"Error en 'delete': {err}")
            return False

    async def get_all(self) -> list[ClienteDomain]:
        lista_cliente = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM cliente")
                result = cursor.fetchall()
                print(result)
                for row in result:
                    cliente = ClienteDomain(
                        idCliente=row['idCliente'],
                        nombre=row['nombre'],
                        direccion=row['direccion'],
                        telefono=row['telefono'],
                        email=row['email'],
                        password=row['password']
                    )
                    lista_cliente.append(cliente)
            return lista_cliente
        except Exception as err:
            print(f"Error en 'get_all': {err}")
            return []


