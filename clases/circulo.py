from clases.figura import figura

class circulo:
    def __init__(self, diametro,color):
        self.color= color
        self.diametro = diametro
    def str__(self):
        return f'Circulo de diametro {self.diametro} y color {self.color}'



