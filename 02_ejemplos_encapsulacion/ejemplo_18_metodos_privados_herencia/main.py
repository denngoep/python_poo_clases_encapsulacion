# Ejemplo 18: Métodos privados en herencia


class Base:

    def __init__(self):

        self.publico = (
            "Accesible para todos"
        )


    def metodo_publico(self):

        print(
            "Método público llamando "
            "a método privado:"
        )

        self.__metodo_privado()


    def __metodo_privado(self):

        print(
            "Este es un método "
            "privado de Base"
        )


class Derivada(Base):

    def nuevo_metodo(self):

        print(
            "Intentando llamar al método "
            "privado del padre:"
        )


        try:
            self.__metodo_privado()

        except AttributeError as e:
            print(f"Error: {e}")


    def __metodo_privado(self):

        print(
            "Este es un método "
            "privado de Derivada"
        )


base = Base()

base.metodo_publico()


derivada = Derivada()

derivada.metodo_publico()

derivada.nuevo_metodo()