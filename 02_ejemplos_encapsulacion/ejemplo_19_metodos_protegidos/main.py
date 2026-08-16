# Ejemplo 19: Métodos protegidos
# utilizados mediante herencia


class Forma:

    def __init__(self):

        self._tipo = "Forma genérica"


    def calcular_area(self):

        return self._obtener_area()


    def _obtener_area(self):

        raise NotImplementedError(
            "Las subclases deben "
            "implementar este método"
        )


    def _validar_dimensiones(
        self,
        valor
    ):

        if (
            not isinstance(
                valor,
                (int, float)
            )
            or valor <= 0
        ):

            raise ValueError(
                "Las dimensiones deben "
                "ser números positivos"
            )

        return True


class Circulo(Forma):

    def __init__(self, radio):

        super().__init__()

        self._tipo = "Círculo"

        self._validar_dimensiones(
            radio
        )

        self._radio = radio


    def _obtener_area(self):

        import math

        return (
            math.pi
            * self._radio ** 2
        )


class Rectangulo(Forma):

    def __init__(
        self,
        ancho,
        alto
    ):

        super().__init__()

        self._tipo = "Rectángulo"


        self._validar_dimensiones(
            ancho
        )

        self._validar_dimensiones(
            alto
        )


        self._ancho = ancho
        self._alto = alto


    def _obtener_area(self):

        return (
            self._ancho
            * self._alto
        )


circulo = Circulo(5)

rectangulo = Rectangulo(
    4,
    3
)


print(
    f"Área del círculo: "
    f"{circulo.calcular_area():.2f}"
)

print(
    f"Área del rectángulo: "
    f"{rectangulo.calcular_area()}"
)