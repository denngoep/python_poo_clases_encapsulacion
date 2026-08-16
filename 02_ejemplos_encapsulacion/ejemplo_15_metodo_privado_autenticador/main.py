# Ejemplo 15: Métodos privados


class Autenticador:

    def __init__(
        self,
        usuario,
        contrasena
    ):

        self._usuario = usuario

        self._contrasena_hash = (
            self.__generar_hash(
                contrasena
            )
        )


    # Método privado.
    def __generar_hash(
        self,
        contrasena
    ):

        import hashlib

        return hashlib.sha256(
            contrasena.encode()
        ).hexdigest()


    # Método público.
    def verificar_contrasena(
        self,
        contrasena_ingresada
    ):

        hash_ingresado = (
            self.__generar_hash(
                contrasena_ingresada
            )
        )

        return (
            hash_ingresado
            == self._contrasena_hash
        )


autenticador = Autenticador(
    "admin",
    "123456"
)


print(
    autenticador.verificar_contrasena(
        "123456"
    )
)

print(
    autenticador.verificar_contrasena(
        "incorrecta"
    )
)