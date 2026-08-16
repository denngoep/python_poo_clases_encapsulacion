# Ejemplo 10: Getter, setter y deleter


class Persona:

    def __init__(self, nombre):

        self._nombre = nombre
        self._amigos = []


    @property
    def nombre(self):

        return self._nombre


    @nombre.setter
    def nombre(self, valor):

        if (
            not isinstance(valor, str)
            or not valor
        ):
            raise ValueError(
                "El nombre debe ser una cadena no vacía"
            )

        self._nombre = valor


    @property
    def amigos(self):

        # Retornamos una copia de la lista.
        return self._amigos.copy()


    @amigos.deleter
    def amigos(self):

        self._amigos = []

        print(
            "Lista de amigos eliminada"
        )


p = Persona("Carlos")


print(p.nombre)


p.nombre = "Carlos Rodríguez"

print(p.nombre)


amigos = p.amigos
amigos.append("Ana")


# La lista original continúa vacía.
print(p.amigos)


# Ejecutamos el deleter.
del p.amigos