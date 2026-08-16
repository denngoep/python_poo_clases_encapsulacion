# Ejemplo 3: Clase Persona con constructor
# Tema: Clases, objetos y método __init__


# Se crea una clase llamada Persona.
class Persona:

    # __init__ es el constructor de la clase.
    # Se ejecuta automáticamente cada vez que
    # se crea un nuevo objeto de tipo Persona.
    def __init__(self, nombre, edad):

        # self.nombre crea el atributo nombre
        # y guarda el valor recibido en el parámetro nombre.
        self.nombre = nombre

        # self.edad crea el atributo edad
        # y guarda el valor recibido en el parámetro edad.
        self.edad = edad


# Creamos un objeto de la clase Persona.
# "Ana García" se guarda en nombre
# y 28 se guarda en edad.
valentina = Persona("Valentina García", 28)


# Creamos un segundo objeto de la misma clase.
marcela = Persona("Marcela Oliveros", 25)


# Accedemos a los atributos de cada objeto
# utilizando la notación de punto.
print("Nombre de la primera persona:", valentina.nombre)
print("Edad de la primera persona:", valentina.edad)

print("Nombre de la segunda persona:", marcela.nombre)
print("Edad de la segunda persona:", marcela.edad)