# Ejemplo 18: Gestión de atributos con funciones integradas


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Creamos una persona.
p = Persona("Laura", 29)


# hasattr verifica si existe un atributo.
print(hasattr(p, "nombre"))
print(hasattr(p, "apellido"))


# getattr obtiene el valor de un atributo.
print(getattr(p, "nombre"))


# Si el atributo no existe podemos establecer
# un valor predeterminado.
print(
    getattr(
        p,
        "apellido",
        "No especificado"
    )
)


# setattr crea o modifica un atributo.
setattr(p, "apellido", "García")

print(p.apellido)


# delattr elimina un atributo.
delattr(p, "apellido")