# Ejemplo 9: Propiedades con @property


class Temperatura:

    def __init__(self, celsius=0):

        self._celsius = celsius


    @property
    def celsius(self):

        return self._celsius


    @celsius.setter
    def celsius(self, valor):

        if valor < -273.15:
            raise ValueError(
                "La temperatura no puede ser "
                "menor que el cero absoluto"
            )

        self._celsius = valor


    @property
    def fahrenheit(self):

        return self._celsius * 9 / 5 + 32


    @fahrenheit.setter
    def fahrenheit(self, valor):

        celsius = (valor - 32) * 5 / 9

        if celsius < -273.15:
            raise ValueError(
                "La temperatura no puede ser "
                "menor que el cero absoluto"
            )

        self._celsius = celsius


temp = Temperatura(25)


print(
    f"Temperatura: "
    f"{temp.celsius}°C"
)

print(
    f"Temperatura: "
    f"{temp.fahrenheit}°F"
)


temp.celsius = 30

print(
    f"Nueva temperatura: "
    f"{temp.celsius}°C"
)

print(
    f"Nueva temperatura: "
    f"{temp.fahrenheit}°F"
)


temp.fahrenheit = 68

print(
    f"Temperatura actualizada: "
    f"{temp.celsius}°C"
)


try:
    temp.celsius = -300

except ValueError as e:
    print(f"Error: {e}")