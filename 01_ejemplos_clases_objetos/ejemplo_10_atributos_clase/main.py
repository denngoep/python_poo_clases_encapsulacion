# Ejemplo 10: Atributos de clase
# Tema: Atributos en Programación Orientada a Objetos


# Se crea la clase Estudiante.
class Estudiante:

    # Este es un atributo de clase.
    # Es compartido por todos los objetos de la clase Estudiante.
    universidad = "Universidad Autónoma"

    # Constructor de la clase.
    def __init__(self, nombre, edad):

        # Estos son atributos de instancia.
        # Cada estudiante tendrá sus propios valores.
        self.nombre = nombre
        self.edad = edad


# Creamos dos objetos de la clase Estudiante.
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)


# Ambos estudiantes comparten el mismo atributo de clase.
print(estudiante1.universidad)
print(estudiante2.universidad)

# También podemos acceder al atributo directamente desde la clase.
print(Estudiante.universidad)


# Modificamos el atributo de clase.
Estudiante.universidad = "Universidad Complutense"


# El cambio se refleja en los objetos.
print(estudiante1.universidad)
print(estudiante2.universidad)