import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.controllers.cliente_controller import cliente_controller
from src.presentation.controllers.producto_controller import producto_controller
from src.presentation.controllers.delivery_controller import delivery_controller
from src.presentation.controllers.pedido_controller import pedido_controller
from src.presentation.controllers.detallepedido_controller import detalle_pedido_controller


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_route(cliente_controller)
app.include_route(producto_controller)
app.include_route(delivery_controller)
app.include_route(pedido_controller)
app.include_route(detalle_pedido_controller)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")

