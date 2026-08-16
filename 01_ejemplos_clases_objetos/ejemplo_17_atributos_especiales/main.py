# Ejemplo 17: Atributos especiales


class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""

    def __init__(self, valor):
        self.valor = valor


# Creamos una instancia.
obj = Ejemplo(42)


# Muestra la clase a la que pertenece el objeto.
print(obj.__class__)


# Muestra el nombre de la clase.
print(Ejemplo.__name__)


# Muestra la documentación de la clase.
print(Ejemplo.__doc__)


# Muestra los atributos de instancia
# almacenados en forma de diccionario.
print(obj.__dict__)