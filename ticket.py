from compra import Compra


class Ticket:
    def __init__(self) -> object:
        self.compra: Compra
    
    def _crear_compra(self):
        self.compra = Compra()
        self.compra._crear_compra()
        self.compra._get_cantidad()

    def imprimir_ticket(self):
        print(self.compra.comprador.nombre)
        print(self.compra.comprador.tarjeta)
        print(self.compra.producto.nombre)
        print(self.compra.cantidad)
        print(self.compra.producto.precio)
        print(self.compra.producto.precio * self.compra.cantidad)