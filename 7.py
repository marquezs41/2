class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

cuenta1 = CuentaBancaria("123456", ["Juan", "María"], 1000.0)
cuenta2 = CuentaBancaria("789012", ["Carlos"], 500.0)

print(f'Cuenta 1: Número de cuenta = {cuenta1.numero_cuenta}, Propietarios = {cuenta1.propietarios}, Balance = {cuenta1.balance}')
print(f'Cuenta 2: Número de cuenta = {cuenta2.numero_cuenta}, Propietarios = {cuenta2.propietarios}, Balance = {cuenta2.balance}')
