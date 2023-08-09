class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, punto1, punto2):
        self.esquina_superior_izquierda = punto1
        self.esquina_inferior_derecha = punto2

    def calcular_perímetro(self):
        base = abs(self.esquina_inferior_derecha.x - self.esquina_superior_izquierda.x)
        altura = abs(self.esquina_inferior_derecha.y - self.esquina_superior_izquierda.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inferior_derecha.x - self.esquina_superior_izquierda.x)
        altura = abs(self.esquina_inferior_derecha.y - self.esquina_superior_izquierda.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inferior_derecha.x - self.esquina_superior_izquierda.x)
        altura = abs(self.esquina_inferior_derecha.y - self.esquina_superior_izquierda.y)
        return base == altura


punto1 = Punto(1, 3)
punto2 = Punto(5, 1)
rectangulo = Rectángulo(punto1, punto2)

print(f'Perímetro del rectángulo: {rectangulo.calcular_perímetro()}')
print(f'Área del rectángulo: {rectangulo.calcular_area()}')
print(f'¿Es un cuadrado?: {rectangulo.es_cuadrado()}')
