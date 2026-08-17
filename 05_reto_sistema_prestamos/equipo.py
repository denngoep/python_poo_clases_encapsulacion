# Clase Equipo
# Representa cada equipo disponible en el sistema.


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre

        # Atributo encapsulado.
        self._disponible = True

        # Lista para almacenar el historial de préstamos.
        self.historial_prestamos = []

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True

        return False

    def devolver(self):
        if not self._disponible:
            self._disponible = True
            return True

        return False

    def agregar_prestamo_historial(self, prestamo):
        self.historial_prestamos.append(prestamo)

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"

        return f"{self.nombre} - {estado}"