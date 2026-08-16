# Ejemplo 12: Modificación de atributos
# Tema: Atributos


class Coche:

    def __init__(self, marca, modelo, color):

        # Atributos recibidos por el constructor.
        self.marca = marca
        self.modelo = modelo
        self.color = color

        # El kilometraje comienza en cero.
        self.kilometraje = 0


# Creamos un coche.
mi_coche = Coche("Toyota", "Corolla", "Azul")


# Mostramos los valores iniciales.
print(f"Color inicial: {mi_coche.color}")
print(f"Kilometraje inicial: {mi_coche.kilometraje}")


# Modificamos los atributos después de crear el objeto.
mi_coche.color = "Rojo"
mi_coche.kilometraje = 1500


# Mostramos los nuevos valores.
print(f"Nuevo color: {mi_coche.color}")
print(f"Kilometraje actual: {mi_coche.kilometraje}")