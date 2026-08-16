# Ejemplo 6: Atributos con validación
# Tema: Clases, objetos y constructor __init__

# Se crea la clase Cuenta.
class Cuenta:

       # El constructor recibe el titular de la cuenta
    # y el saldo inicial.
    def __init__(self, titular, saldo_inicial):

     # Se guarda el nombre del titular.
        self.titular = titular

        # Se valida que el saldo inicial no sea negativo.
        # Si es menor que 0, se genera un error ValueError.
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        # Si el saldo es válido, se guarda en el objeto.
        self.saldo = saldo_inicial   

# Creamos una cuenta con un saldo válido.
cuenta_ana = Cuenta("Ana García", 1000)

# Mostramos los datos de la cuenta.
print("Titular:", cuenta_ana.titular)
print("Saldo:", cuenta_ana.saldo)


# Intentamos crear una cuenta con saldo negativo.
# try permite intentar ejecutar un código que podría generar un error.
try:
    cuenta_problematica = Cuenta("Juan López", -500)

# Si se produce un ValueError, se captura aquí.
except ValueError as e:
    print(f"Error: {e}")