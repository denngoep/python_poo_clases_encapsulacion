# Ejemplo 15: Propiedades
# Tema: @property y setter


class Temperatura:

    def __init__(self):

        # Atributo protegido.
        self._celsius = 0


    # Propiedad para obtener Celsius.
    @property
    def celsius(self):
        return self._celsius


    # Setter para modificar Celsius.
    @celsius.setter
    def celsius(self, valor):

        # Validamos que la temperatura
        # no sea inferior al cero absoluto.
        if valor < -273.15:
            raise ValueError(
                "La temperatura no puede ser menor que el cero absoluto"
            )

        self._celsius = valor


    # Propiedad calculada para Fahrenheit.
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


    # Setter para establecer Fahrenheit.
    @fahrenheit.setter
    def fahrenheit(self, valor):

        # Convertimos Fahrenheit a Celsius.
        self.celsius = (valor - 32) * 5 / 9


# Creamos una temperatura.
temp = Temperatura()


# Establecemos Celsius.
temp.celsius = 25

print(f"{temp.celsius}°C = {temp.fahrenheit}°F")


# Establecemos Fahrenheit.
temp.fahrenheit = 68

print(f"{temp.celsius}°C = {temp.fahrenheit}°F")


# Probamos la validación.
try:
    temp.celsius = -300

except ValueError as e:
    print(f"Error: {e}")