from clases.figura import figura

class elipse:
    def __init__(self, eje_mayor, eje_menor, color):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        super().__init__(color)