# Ejemplo 13: Atributos dinámicos
# Tema: Atributos


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


# Creamos una persona.
juan = Persona("Juan")


# Añadimos nuevos atributos después
# de haber creado el objeto.
juan.edad = 30
juan.profesion = "Ingeniero"


# Mostramos la información.
print(
    f"{juan.nombre} tiene {juan.edad} años "
    f"y es {juan.profesion}"
)