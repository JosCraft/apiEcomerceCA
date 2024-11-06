from src.core.abstractions.infrastructure.repository.example_repository_abstract import IExampleRepository
from src.core.models.example_domain import ExampleDomain

class ExampleRepository(IExampleRepository):

    def __init__(self, connection):
        self.connection = connection

    def get_example(self, example_id: int) -> ExampleDomain:
        color = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM catematerial")
                result = cursor.fetchone()
                color = ExampleDomain(
                    id=result["id_cl"],
                    nombre=result["nombre_cl"],
                    codigoHex=result["codigo_hx"]
                )
                return color
        except Exception as e:
            print(e)
        return color
