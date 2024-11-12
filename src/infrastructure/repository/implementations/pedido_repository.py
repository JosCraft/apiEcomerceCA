
from src.core.abstractions.infrastructure.repository.pedido_repository_abstract import IPedidoRepository
from src.core.models.pedido_domain import PedidoDomain

class PedidoRepository(IPedidoRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get(self, id: int) -> PedidoDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM pedido WHERE idPedido = %s", (id,))
                result = cursor.fetchone()
                if result:
                    return PedidoDomain(
                        idPedido=result['idPedido'],
                        fecha=result['fecha'],
                        estado=result['estado'],
                        total=result['total'],
                        idCliente=result['idCliente'],
                    )
        except Exception as error:
            print(f"Error: {error}")
        return None

    async def create(self, pedido: PedidoDomain) -> PedidoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO pedido (fecha, estado, total, idCliente)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        pedido.fecha,
                        pedido.estado,
                        pedido.total,
                        pedido.idCliente
                    )
                )
                self.connection.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]
                # Return the newly created PedidoDomain with the last inserted ID
                return PedidoDomain(
                    idPedido=last_id,
                    fecha=pedido.fecha,
                    estado=pedido.estado,
                    total=pedido.total,
                    idCliente=pedido.idCliente
                )
        except Exception as error:
            print(f"Error: {error}")
            return None

    async def update(self, idPedido: int, pedido: PedidoDomain) -> PedidoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE pedido
                    SET fecha = %s, estado = %s, total = %s, idCliente = %s
                    WHERE idPedido = %s
                    """,
                    (
                        pedido.fecha,
                        pedido.estado,
                        pedido.total,
                        pedido.idCliente,
                        idPedido
                    )
                )
                self.connection.commit()
                if cursor.rowcount > 0:
                    return pedido  # Return the updated PedidoDomain
                return None
        except Exception as error:
            print(f"Error: {error}")
            return None

    async def delete(self, id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM pedido WHERE idPedido = %s",
                    (id,)
                )
                self.connection.commit()
                return cursor.rowcount > 0
        except Exception as err:
            print(f"Error: {err}")
            return False

    async def get_all(self) -> list[PedidoDomain]:
        lista_pedido = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM pedido")
                result = cursor.fetchall()
                for row in result:
                    pedido = PedidoDomain(
                        idPedido=row['idPedido'],
                        fecha=row['fecha'],
                        estado=row['estado'],
                        total=row['total'],
                        idCliente=row['idCliente']
                    )
                    lista_pedido.append(pedido)
            return lista_pedido
        except Exception as error:
            print(f"Error: {error}")
            return []
