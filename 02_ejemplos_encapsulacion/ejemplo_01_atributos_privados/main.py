# Ejemplo 1: Atributos privados por convención
# Tema: Encapsulación


class CuentaBancaria:

    def __init__(self, titular, saldo_inicial):

        # El guion bajo indica que estos atributos
        # deben tratarse como privados por convención.
        self._titular = titular
        self._saldo = saldo_inicial


    def depositar(self, cantidad):

        if cantidad > 0:
            self._saldo += cantidad
            return True

        return False


# Creamos una cuenta.
cuenta = CuentaBancaria("Ana García", 1000)


# Técnicamente podemos acceder al atributo,
# aunque no es recomendable hacerlo directamente.
print(cuenta._saldo)