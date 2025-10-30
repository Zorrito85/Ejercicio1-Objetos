from clases.figura import figuras

class circulo(figuras):
    def __init__(self,color, diametro):
        super().__init__(color)
        self.diametro = diametro
    def str__(self):
        return f'Circulo de diametro {self.diametro} y color {self.color}'



