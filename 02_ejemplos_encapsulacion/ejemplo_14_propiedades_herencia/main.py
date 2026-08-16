# Ejemplo 14: Propiedades en clases heredadas


class Producto:

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


    @property
    def info(self):

        return (
            f"{self._nombre}: "
            f"{self._precio}€"
        )


class ProductoDigital(Producto):

    def __init__(
        self,
        nombre,
        precio,
        tamano_mb
    ):

        super().__init__(
            nombre,
            precio
        )

        self._tamano_mb = tamano_mb


    @property
    def tamano_mb(self):

        return self._tamano_mb


    @tamano_mb.setter
    def tamano_mb(self, valor):

        if valor <= 0:
            raise ValueError(
                "El tamaño debe ser positivo"
            )

        self._tamano_mb = valor


    @property
    def info(self):

        return (
            f"{self._nombre}: "
            f"{self._precio}€ "
            f"({self._tamano_mb} MB)"
        )


p1 = Producto(
    "Teclado",
    49.99
)

p2 = ProductoDigital(
    "Ebook Python",
    19.99,
    15.5
)


print(p1.info)
print(p2.info)


p2.tamano_mb = 20
p2.precio = 24.99


print(p2.info)