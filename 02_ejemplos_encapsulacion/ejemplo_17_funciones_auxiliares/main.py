# Ejemplo 17: Métodos privados
# vs funciones auxiliares


class Ejemplo1:

    def metodo_publico(
        self,
        datos
    ):

        # Función auxiliar interna.
        def funcion_auxiliar(x):

            return x * 2


        resultado = [
            funcion_auxiliar(x)
            for x in datos
        ]

        return resultado


class Ejemplo2:

    def metodo_publico(
        self,
        datos
    ):

        resultado = [
            self.__funcion_auxiliar(x)
            for x in datos
        ]

        return resultado


    def __funcion_auxiliar(
        self,
        x
    ):

        return x * 2


e1 = Ejemplo1()
e2 = Ejemplo2()


print(
    e1.metodo_publico(
        [1, 2, 3]
    )
)

print(
    e2.metodo_publico(
        [1, 2, 3]
    )
)