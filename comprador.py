class Comprador:
    # Informacion del comprador
    def __init__(self) -> object:
        self.nombre: str
        self.tarjeta: str
    
    def _info_comprador(self):
        self.nombre = input('Ingresa tu nombre 😊: ')
        self.tarjeta = input('Ingresa tu tarjeta 😊: ')
