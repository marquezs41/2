class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

PINTA_CORAZON = "Corazón"
PINTA_DIAMANTE = "Diamante"
PINTA_TREBOL = "Trébol"
PINTA_PICA = "Pica"

carta1 = Carta("As", PINTA_CORAZON)
carta2 = Carta("10", PINTA_DIAMANTE)

print(f'Carta 1: Valor = {carta1.valor}, Pinta = {carta1.pinta}')
print(f'Carta 2: Valor = {carta2.valor}, Pinta = {carta2.pinta}')
