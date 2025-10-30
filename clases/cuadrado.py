from clases.figura import figuras

class cuadrado(figuras):
    def __init__(self, lado, color):
        self.lado= lado
        super().__init__(color)

    def str__(self):
        return f'Cuadrado de lado {self.lado} y color {self.color}'