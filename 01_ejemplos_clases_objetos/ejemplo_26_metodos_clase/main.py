# Ejemplo 26: Métodos de clase


class Empleado:

    # Atributo de clase que cuenta
    # los empleados creados.
    num_empleados = 0


    def __init__(self, nombre, salario):

        self.nombre = nombre
        self.salario = salario

        # Cada vez que se crea un empleado,
        # aumentamos el contador.
        Empleado.num_empleados += 1


    @classmethod
    def desde_salario_anual(
        cls,
        nombre,
        salario_anual
    ):

        # Convertimos el salario anual en mensual.
        salario_mensual = salario_anual / 12

        # Creamos y devolvemos un nuevo empleado.
        return cls(nombre, salario_mensual)


    @classmethod
    def obtener_num_empleados(cls):

        return cls.num_empleados


# Creación normal.
emp1 = Empleado("Ana", 3000)


# Constructor alternativo.
emp2 = Empleado.desde_salario_anual(
    "Carlos",
    48000
)


print(
    f"Empleados creados: "
    f"{Empleado.obtener_num_empleados()}"
)