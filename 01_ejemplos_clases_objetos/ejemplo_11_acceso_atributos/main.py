# Ejemplo 11: Acceso a atributos
# Tema: Atributos en Programación Orientada a Objetos


# Se crea la clase Producto.
class Producto:

    # Atributo de clase compartido por todos los productos.
    impuesto = 0.21

    # Constructor de la clase.
    def __init__(self, nombre, precio):

        # Atributos de instancia.
        self.nombre = nombre
        self.precio = precio


# Creamos un objeto de la clase Producto.
laptop = Producto("Laptop", 1000)


# Accedemos a los atributos de instancia
# utilizando el nombre del objeto y la notación de punto.
print(laptop.nombre)
print(laptop.precio)


# Accedemos al atributo de clase desde el objeto.
print(laptop.impuesto)


# También podemos acceder al atributo de clase
# directamente utilizando el nombre de la clase.
print(Producto.impuesto)