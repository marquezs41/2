class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    
punto1 = Punto(3, 4)

print(f'Coordenadas del punto 1: {punto1}')
