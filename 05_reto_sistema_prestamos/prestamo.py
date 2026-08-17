# Clase Prestamo
# Representa la relación entre un usuario y un equipo.


class Prestamo:
    def __init__(self, usuario, equipo, fecha):
        self.usuario = usuario
        self.equipo = equipo
        self.fecha = fecha

        # Estado encapsulado.
        self._activo = True

    @property
    def activo(self):
        return self._activo

    def devolver(self):
        if self._activo:
            self._activo = False
            return True

        return False

    def modificar_fecha(self, nueva_fecha):
        self.fecha = nueva_fecha

    def __str__(self):
        estado = "Activo" if self._activo else "Devuelto"

        return (
            f"Usuario: {self.usuario.nombre} | "
            f"Equipo: {self.equipo.nombre} | "
            f"Fecha: {self.fecha} | "
            f"Estado: {estado}"
        )