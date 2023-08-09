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

cuenta = CuentaBancaria("123456", ["Juan", "María"], 1000.0)
print(f'Balance inicial: {cuenta.balance}')

cuenta.depositar(500)
cuenta.depositar(-100)  
