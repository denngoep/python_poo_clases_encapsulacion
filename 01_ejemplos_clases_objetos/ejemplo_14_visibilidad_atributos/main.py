# Ejemplo 14: Atributos públicos, protegidos y privados
# Tema: Atributos


class CuentaBancaria:

    # Atributo de clase público.
    tasa_interes = 0.03

    def __init__(self, titular, saldo_inicial, pin):

        # Atributo público.
        self.titular = titular

        # Atributo protegido por convención.
        self._saldo = saldo_inicial

        # Atributo privado.
        self.__pin = pin

    # Método que permite verificar el PIN.
    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado


# Creamos una cuenta.
cuenta = CuentaBancaria("Ana López", 1000, "1234")


# Atributo público.
print(cuenta.titular)

# Funciona, aunque por convención no deberíamos
# acceder directamente al atributo protegido.
print(cuenta._saldo)

# Acceso al atributo privado mediante name mangling.
# Funciona, pero es una mala práctica.
print(cuenta._CuentaBancaria__pin)