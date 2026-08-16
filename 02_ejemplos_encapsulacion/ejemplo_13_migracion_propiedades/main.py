# Ejemplo 13: Migración de getters y setters
# a propiedades


# Versión 1: atributos públicos.
class ProductoV1:

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio


# Versión 2: getters y setters.
class ProductoV2:

    def __init__(self, nombre, precio):

        self._nombre = nombre
        self._precio = precio


    def get_nombre(self):

        return self._nombre


    def set_nombre(self, valor):

        self._nombre = valor


    def get_precio(self):

        return self._precio


    def set_precio(self, valor):

        if valor < 0:
            raise ValueError(
                "El precio no puede ser negativo"
            )

        self._precio = valor


# Versión 3: propiedades.
class ProductoV3:

    def __init__(self, nombre, precio):

        self._nombre = nombre
        self._precio = precio


    @property
    def nombre(self):

        return self._nombre


    @nombre.setter
    def nombre(self, valor):

        self._nombre = valor


    @property
    def precio(self):

        return self._precio


    @precio.setter
    def precio(self, valor):

        if valor < 0:
            raise ValueError(
                "El precio no puede ser negativo"
            )

        self._precio = valor


# Probamos las tres versiones.
p1 = ProductoV1("Mouse", 50)

p2 = ProductoV2("Teclado", 80)

p3 = ProductoV3("Monitor", 300)


print(p1.nombre, p1.precio)

print(
    p2.get_nombre(),
    p2.get_precio()
)

print(
    p3.nombre,
    p3.precio
)