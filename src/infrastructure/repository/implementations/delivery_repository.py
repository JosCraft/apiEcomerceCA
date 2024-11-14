from src.core.abstractions.infrastructure.repository.delivery_repository_abstract import IDeliveryRepository
from src.core.models.delivery_domain import DeliveryDomain

class deliveryRepository(IDeliveryRepository):
    def __init__(self,connection):
        self.connection=connection
    async def get(self, id: int) -> DeliveryDomain:
        print('ither ',id)
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM delivery where idDelivery=%s",(id,))
                result = cursor.fetchone()
                print(result)
                         #cursor.fetchall()
                return DeliveryDomain(
                    idDelivery= result['idDelivery'],
                    nombre= result['nombre'],
                    turno= result['turno'],
                    email= result['email'],
                    estado= result['estado'],
                    ubicacion= result['ubicacion'],
                    password=result['password'],
                )
        except Exception as error:
            print(f"Error: {error}")
        return None

    async def get_delivery_by_email(self, email: str) -> DeliveryDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM delivery WHERE email=%s", (email,))
                result = cursor.fetchone()
                if result:
                    return DeliveryDomain(
                        idDelivery=result['idDelivery'],
                        nombre=result['nombre'],
                        turno=result['turno'],
                        email=result['email'],
                        estado=result['estado'],
                        ubicacion=result['ubicacion'],
                        password=result['password'],
                        # Recuerda usar hashing de contraseñas
                    )
        except Exception as error:
            print(f"Error en 'get_delivery_by_email': {error}")
        return None
    async def create(self, delivery: DeliveryDomain) -> DeliveryDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO delivery (nombre, turno, email, estado, ubicacion, password)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        delivery.nombre,
                        delivery.turno,
                        delivery.email,
                        delivery.estado,
                        delivery.ubicacion,
                        delivery.password
                    )
                )
                self.connection.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]
            return last_id
        except Exception as error:
            print(f"Error: {error}")
            return None
        pass

    async def update(self, idDelivery:int, delivery: DeliveryDomain) -> DeliveryDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE delivery 
                    SET nombre = %s, turno = %s, email = %s, estado = %s, ubicacion = %s, password = %s
                    WHERE idDelivery = %s
                    """,
                    (
                        delivery.nombre,
                        delivery.turno,
                        delivery.email,
                        delivery.estado,
                        delivery.ubicacion,
                        delivery.password,
                        idDelivery
                    )
                )
                self.connection.commit()
                return cursor.rowcount > 0
        except Exception as error:
            print(f"Error: {error}")
            return False
        pass

    async def delete(self, id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM delivery WHERE idDelivery = %s",
                    (id,)
                )
                self.connection.commit()
                return cursor.rowcount > 0
        except Exception as err:
            print(f"Error: {err}")
            return False
        pass

    async def get_all(self) -> list[DeliveryDomain]:
        lista_delivery = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM delivery")
                result = cursor.fetchall()
                for row in result:
                    delivery = DeliveryDomain(
                        idDelivery=row['idDelivery'],
                        nombre=row['nombre'],
                        turno=row['turno'],
                        email=row['email'],
                        estado=row['estado'],
                        ubicacion=row['ubicacion'],
                        password=row['password']
                    )
                    lista_delivery.append(delivery)
            return lista_delivery
        except Exception as error:
            print(f"Error: {error}")
            return []