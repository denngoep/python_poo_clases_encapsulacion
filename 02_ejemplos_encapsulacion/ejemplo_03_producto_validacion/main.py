# Ejemplo 3: Validación de datos
# Tema: Atributos privados


class Producto:

    def __init__(self, nombre, precio):

        self._nombre = nombre

        # Validamos el precio antes de guardarlo.
        if precio < 0:
            raise ValueError(
                "El precio no puede ser negativo"
            )

        self._precio = precio


# Creamos un producto válido.
producto = Producto("Teclado", 80)

print(producto._nombre)
print(producto._precio)


# Intentamos crear un producto inválido.
try:
    producto_error = Producto("Mouse", -50)

except ValueError as e:
    print(f"Error: {e}")