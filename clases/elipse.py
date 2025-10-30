from clases.figura import figuras

class elipse(figuras):
    def __init__(self, eje_mayor, eje_menor, color):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        super().__init__(color)
    def str__(self):
        return f'Elipse de eje mayor {self.eje_mayor}, eje menor {self.eje_menor} y color {self.color}'