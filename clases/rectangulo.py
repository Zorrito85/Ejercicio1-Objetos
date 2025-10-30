from clases.figura import figuras
class rectangulo(figuras):
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        super().__init__(color)
        

    def str__(self):
        return f'Rectangulo de base {self.base}, altura {self.altura} y color {self.color}'