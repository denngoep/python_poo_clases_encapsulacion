# Ejemplo 9: Atributos de instancia
# Tema: Atributos en Programación Orientada a Objetos


# Se crea la clase Estudiante.
class Estudiante:

    # El constructor recibe el nombre y la edad.
    def __init__(self, nombre, edad):

        # Estos son atributos de instancia.
        # Cada objeto tendrá sus propios valores.
        self.nombre = nombre
        self.edad = edad

        # Este atributo también es de instancia,
        # pero comienza con un valor predeterminado.
        self.activo = True


# Creamos dos objetos de la clase Estudiante.
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)


# Mostramos los atributos de cada estudiante.
print("Estudiante 1:")
print("Nombre:", estudiante1.nombre)
print("Edad:", estudiante1.edad)
print("Activo:", estudiante1.activo)

print()

print("Estudiante 2:")
print("Nombre:", estudiante2.nombre)
print("Edad:", estudiante2.edad)
print("Activo:", estudiante2.activo)