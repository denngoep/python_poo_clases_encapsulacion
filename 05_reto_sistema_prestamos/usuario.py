# Clase Usuario
# Representa a la persona que solicita un equipo.


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

        # Lista de préstamos asociados al usuario.
        self.prestamos = []

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def __str__(self):
        return self.nombre