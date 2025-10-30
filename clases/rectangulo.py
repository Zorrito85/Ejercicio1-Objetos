from clases.figura import figura
class rectangulo:
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        super().__init__(color)