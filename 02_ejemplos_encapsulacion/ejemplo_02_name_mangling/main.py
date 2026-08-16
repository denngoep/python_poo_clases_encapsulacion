# Ejemplo 2: Atributos privados con doble guion bajo
# Tema: Name mangling


class CuentaBancaria:

    def __init__(self, titular, saldo_inicial, pin):

        self._titular = titular
        self._saldo = saldo_inicial

        # Atributo privado.
        self.__pin = pin


    def validar_pin(self, pin_ingresado):

        return self.__pin == pin_ingresado


# Creamos una cuenta.
cuenta = CuentaBancaria(
    "Ana García",
    1000,
    "1234"
)


# Intentamos acceder directamente al PIN.
try:
    print(cuenta.__pin)

except AttributeError as e:
    print(f"Error: {e}")


# Acceso mediante name mangling.
# Funciona, aunque es una mala práctica.
print(cuenta._CuentaBancaria__pin)