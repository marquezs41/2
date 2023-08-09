class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

auto = Vehículo(200, 50000)

print("Velocidad máxima:", auto.velocidad_maxima)
print("Kilometraje:", auto.kilometraje)

