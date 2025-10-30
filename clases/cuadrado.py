from clases.figura import figura

class cuadrado:
    def __init__(self, lado, color):
        self.lado= lado
        self.color=color

    def str__(self):
        return f'Cuadrado de lado {self.lado} y color {self.color}'