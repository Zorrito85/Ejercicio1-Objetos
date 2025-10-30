from clases.figura import figura
class rectangulo:
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color
        

    def str__(self):
        return f'Rectangulo de base {self.base}, altura {self.altura} y color {self.color}'