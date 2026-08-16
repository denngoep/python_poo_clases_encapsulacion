# Ejemplo 7: Getters y setters en herencia


class Producto:

    def __init__(self, nombre, precio, stock=0):

        self._nombre = nombre
        self._precio = precio
        self._stock = stock


    def set_precio(self, nuevo_precio):

        if (
            not isinstance(
                nuevo_precio,
                (int, float)
            )
            or nuevo_precio < 0
        ):
            raise ValueError(
                "El precio debe ser un número positivo"
            )

        self._precio = nuevo_precio


class Electronico(Producto):

    def __init__(
        self,
        nombre,
        precio,
        stock,
        garantia_meses
    ):

        super().__init__(
            nombre,
            precio,
            stock
        )

        self._garantia_meses = garantia_meses
        self._activado = False


    def get_garantia_meses(self):

        return self._garantia_meses


    def esta_activado(self):

        return self._activado


    def set_garantia_meses(self, meses):

        if (
            not isinstance(meses, int)
            or meses < 0
        ):
            raise ValueError(
                "Los meses de garantía "
                "deben ser un entero positivo"
            )

        self._garantia_meses = meses


    def activar(self):

        self._activado = True


    def desactivar(self):

        self._activado = False


    def set_precio(self, nuevo_precio):

        # Utilizamos el setter del padre.
        super().set_precio(nuevo_precio)


        # Si es un producto costoso,
        # la garantía mínima será 24 meses.
        if nuevo_precio > 1000:

            self._garantia_meses = max(
                self._garantia_meses,
                24
            )


# Creamos un electrónico.
laptop = Electronico(
    "Laptop",
    900,
    10,
    12
)


print(
    f"Garantía inicial: "
    f"{laptop.get_garantia_meses()} meses"
)


laptop.set_precio(1500)


print(
    f"Garantía después del cambio de precio: "
    f"{laptop.get_garantia_meses()} meses"
)


laptop.activar()

print(
    f"¿Está activado?: "
    f"{laptop.esta_activado()}"
)