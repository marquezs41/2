class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f'Se ha depositado {monto} en la cuenta. Nuevo balance: {self.balance}')
        else:
            print('El monto de depósito debe ser mayor a cero.')

    def retirar(self, monto):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            print(f'Se ha retirado {monto} de la cuenta. Nuevo balance: {self.balance}')
        else:
            print('Monto inválido para el retiro.')

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f'Se ha aplicado una cuota de manejo del 2% ({cuota}) sobre el balance. Nuevo balance: {self.balance}')

cuenta = CuentaBancaria("123456", ["Juan", "María"], 1000.0)
print(f'Balance inicial: {cuenta.balance}')

cuenta.depositar(500)
cuenta.aplicar_cuota_manejo()
cuenta.retirar(300)
