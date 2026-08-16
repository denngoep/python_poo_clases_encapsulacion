# Ejemplo 4: Valores predeterminados en el constructor
# Tema: Clases, objetos y constructor __init__


# Se crea la clase Producto.
class Producto:

    # El constructor recibe nombre, precio y stock.
    # stock tiene un valor predeterminado de 0.
    # Esto significa que no es obligatorio enviarlo al crear el objeto.
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


# Creamos un producto sin especificar el stock.
# Como no enviamos ese dato, Python utiliza el valor predeterminado 0.
laptop = Producto("Laptop XPS", 1200)


# Creamos otro producto indicando el stock.
# En este caso, el valor 15 reemplaza el valor predeterminado.
teclado = Producto("Teclado mecánico", 80, 15)


# Mostramos la información de los productos.
print("Producto:", laptop.nombre)
print("Precio:", laptop.precio)
print("Stock:", laptop.stock)

print()

print("Producto:", teclado.nombre)
print("Precio:", teclado.precio)
print("Stock:", teclado.stock)