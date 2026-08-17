# Taller de Encapsulación
# Caso 1: Cuenta Bancaria
#
# Este programa implementa una clase CuentaBancaria utilizando
# encapsulación para controlar el acceso y modificación de sus datos.


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            titular (str): Nombre del titular de la cuenta.
            saldo_inicial (float): Saldo inicial de la cuenta.
        """

        # Atributo protegido que almacena el nombre del titular.
        self._titular = titular

        # Se utiliza la propiedad saldo para validar el saldo inicial.
        self.saldo = saldo_inicial

    @property
    def titular(self):
        """
        Permite consultar el titular de la cuenta.
        No tiene setter, por lo tanto es una propiedad de solo lectura.
        """
        return self._titular

    @property
    def saldo(self):
        """
        Permite consultar el saldo actual de la cuenta.
        """
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """
        Permite modificar el saldo verificando que no sea negativo.
        """
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")

        self._saldo = float(nuevo_saldo)

    def depositar(self, cantidad):
        """
        Incrementa el saldo cuando la cantidad es positiva.
        """
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            return True

        return False

    def retirar(self, cantidad):
        """
        Disminuye el saldo solamente cuando la cantidad es positiva
        y existe suficiente dinero en la cuenta.
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            return True

        return False


# Prueba de la clase CuentaBancaria
def main():

    # Crear una cuenta bancaria.
    cuenta = CuentaBancaria("Ana García", 1000)

    # Mostrar información inicial.
    print("=== INFORMACIÓN INICIAL ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: ${cuenta.saldo}")

    # Realizar un depósito válido.
    print("\n=== DEPÓSITO ===")

    if cuenta.depositar(500):
        print("Depósito realizado correctamente.")
    else:
        print("No fue posible realizar el depósito.")

    print(f"Saldo actual: ${cuenta.saldo}")

    # Intentar realizar un depósito inválido.
    print("\n=== DEPÓSITO INVÁLIDO ===")

    if cuenta.depositar(-100):
        print("Depósito realizado correctamente.")
    else:
        print("No fue posible realizar el depósito.")

    print(f"Saldo actual: ${cuenta.saldo}")

    # Realizar un retiro válido.
    print("\n=== RETIRO ===")

    if cuenta.retirar(300):
        print("Retiro realizado correctamente.")
    else:
        print("No fue posible realizar el retiro.")

    print(f"Saldo actual: ${cuenta.saldo}")

    # Intentar retirar más dinero del disponible.
    print("\n=== RETIRO SIN FONDOS SUFICIENTES ===")

    if cuenta.retirar(5000):
        print("Retiro realizado correctamente.")
    else:
        print("No fue posible realizar el retiro.")

    print(f"Saldo actual: ${cuenta.saldo}")

    # Probar la validación de la propiedad saldo.
    print("\n=== VALIDACIÓN DE SALDO NEGATIVO ===")

    try:
        cuenta.saldo = -500
    except ValueError as error:
        print(f"Error: {error}")

    # Mostrar información final.
    print("\n=== INFORMACIÓN FINAL ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: ${cuenta.saldo}")


if __name__ == "__main__":
    main()







          
                        

    
