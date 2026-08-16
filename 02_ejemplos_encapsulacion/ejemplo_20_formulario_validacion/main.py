# Ejemplo 20: Validación compleja
# utilizando métodos privados


class Formulario:

    def __init__(self):

        self._datos = {}
        self._errores = {}


    def validar(self, datos):

        self._datos = datos.copy()

        self._errores = {}


        self.__validar_campos_requeridos()

        self.__validar_email()

        self.__validar_contrasena()

        self.__validar_edad()


        return (
            len(self._errores) == 0
        )


    def obtener_errores(self):

        return self._errores.copy()


    def __validar_campos_requeridos(
        self
    ):

        campos_requeridos = [
            "nombre",
            "email",
            "contraseña"
        ]


        for campo in campos_requeridos:

            if (
                campo not in self._datos
                or not self._datos[campo]
            ):

                self._errores[campo] = (
                    f"El campo {campo} "
                    f"es obligatorio"
                )


    def __validar_email(self):

        if (
            "email" in self._datos
            and self._datos["email"]
        ):

            import re

            patron = (
                r"^[a-zA-Z0-9._%+-]+"
                r"@[a-zA-Z0-9.-]+"
                r"\.[a-zA-Z]{2,}$"
            )


            if not re.match(
                patron,
                self._datos["email"]
            ):

                self._errores["email"] = (
                    "El formato del email "
                    "no es válido"
                )


    def __validar_contrasena(self):

        if (
            "contraseña" in self._datos
            and self._datos["contraseña"]
        ):

            contrasena = (
                self._datos["contraseña"]
            )


            if len(contrasena) < 8:

                self._errores[
                    "contraseña"
                ] = (
                    "La contraseña debe tener "
                    "al menos 8 caracteres"
                )


            elif not any(
                c.isupper()
                for c in contrasena
            ):

                self._errores[
                    "contraseña"
                ] = (
                    "La contraseña debe contener "
                    "al menos una mayúscula"
                )


            elif not any(
                c.isdigit()
                for c in contrasena
            ):

                self._errores[
                    "contraseña"
                ] = (
                    "La contraseña debe contener "
                    "al menos un número"
                )


    def __validar_edad(self):

        if "edad" in self._datos:

            try:

                edad = int(
                    self._datos["edad"]
                )


                if edad < 18:

                    self._errores["edad"] = (
                        "Debes ser mayor de edad"
                    )


                elif edad > 120:

                    self._errores["edad"] = (
                        "La edad ingresada "
                        "no es válida"
                    )


            except ValueError:

                self._errores["edad"] = (
                    "La edad debe ser un número"
                )


# Datos de prueba.
datos = {
    "nombre": "Ana",
    "email": "ana@email.com",
    "contraseña": "Clave123",
    "edad": 25
}


formulario = Formulario()


print(
    "Formulario válido:",
    formulario.validar(datos)
)

print(
    "Errores:",
    formulario.obtener_errores()
)