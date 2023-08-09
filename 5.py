import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia_centro_punto <= self.radio

centro = Punto(0, 0)
circulo = Circulo(centro, 5)

print(f'Área del círculo: {circulo.calcular_area()}')
print(f'Perímetro del círculo: {circulo.calcular_perimetro()}')

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

print(f'¿El punto ({punto1.x}, {punto1.y}) pertenece al círculo?: {circulo.punto_pertenece(punto1)}')
print(f'¿El punto ({punto2.x}, {punto2.y}) pertenece al círculo?: {circulo.punto_pertenece(punto2)}')
