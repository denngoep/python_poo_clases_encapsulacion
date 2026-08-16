# Ejemplo 21: Métodos que interactúan con atributos


class CuentaBancaria:

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial


    # Consulta el saldo.
    def consultar_saldo(self):
        return (
            f"Saldo actual de {self.titular}: "
            f"${self._saldo}"
        )


    # Realiza un depósito.
    def depositar(self, cantidad):

        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"

        self._saldo += cantidad

        return (
            f"Depósito de ${cantidad} realizado. "
            f"Nuevo saldo: ${self._saldo}"
        )


    # Realiza un retiro.
    def retirar(self, cantidad):

        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"

        if cantidad > self._saldo:
            return "Fondos insuficientes"

        self._saldo -= cantidad

        return (
            f"Retiro de ${cantidad} realizado. "
            f"Nuevo saldo: ${self._saldo}"
        )


# Creamos la cuenta.
cuenta = CuentaBancaria("Ana López", 1000)


print(cuenta.consultar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(2000))