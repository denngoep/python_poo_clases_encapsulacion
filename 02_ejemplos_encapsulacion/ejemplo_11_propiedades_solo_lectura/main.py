# Ejemplo 11: Propiedades de solo lectura


class Circulo:

    def __init__(self, radio):

        self._radio = radio


    @property
    def radio(self):

        return self._radio


    @radio.setter
    def radio(self, valor):

        if valor <= 0:
            raise ValueError(
                "El radio debe ser positivo"
            )

        self._radio = valor


    @property
    def area(self):

        import math

        return math.pi * self._radio ** 2


    @property
    def perimetro(self):

        import math

        return 2 * math.pi * self._radio


c = Circulo(5)


print(f"Radio: {c.radio}")
print(f"Área: {c.area:.2f}")
print(
    f"Perímetro: {c.perimetro:.2f}"
)


c.radio = 10


print(f"Nuevo radio: {c.radio}")
print(
    f"Nueva área: {c.area:.2f}"
)


try:
    c.area = 100

except AttributeError as e:
    print(f"Error: {e}")