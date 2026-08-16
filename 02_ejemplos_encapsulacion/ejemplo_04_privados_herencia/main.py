# Ejemplo 4: Atributos privados y protegidos
# en herencia


class Vehiculo:

    def __init__(self, marca, modelo):

        # Protegido.
        self._marca = marca

        # Privado.
        self.__modelo = modelo


class Coche(Vehiculo):

    def __init__(self, marca, modelo, puertas):

        # Ejecutamos el constructor de Vehiculo.
        super().__init__(marca, modelo)

        self._puertas = puertas


    def info(self):

        # Podemos acceder al atributo protegido.
        print(f"Marca: {self._marca}")


        # No podemos acceder directamente
        # al atributo privado de la clase padre.
        try:
            print(f"Modelo: {self.__modelo}")

        except AttributeError:
            print(
                "No se puede acceder a __modelo "
                "desde la subclase"
            )


# Creamos un coche.
coche = Coche(
    "Toyota",
    "Corolla",
    4
)

coche.info()