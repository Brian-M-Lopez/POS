from comprador import Comprador
from producto import Producto


class Compra:
    def __init__(self) -> object:
        self.comprador: Comprador
        self.producto: Producto
        self.cantidad: int
        self.id = "0001"

    def _get_cantidad(self):
        self.cantidad = int(input("Cuantos querer comprar? 💲💲💲: "))

    def _crear_compra(self):
        self.comprador = Comprador()
        self.comprador._info_comprador()
        self.producto = Producto()