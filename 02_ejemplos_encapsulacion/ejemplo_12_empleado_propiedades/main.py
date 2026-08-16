# Ejemplo 12: Propiedades calculadas


class Empleado:

    def __init__(
        self,
        nombre,
        salario_base,
        horas_extra=0,
        tarifa_extra=0
    ):

        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra
        self._tarifa_extra = tarifa_extra


    @property
    def nombre(self):

        return self._nombre


    @property
    def salario_base(self):

        return self._salario_base


    @salario_base.setter
    def salario_base(self, valor):

        if valor < 0:
            raise ValueError(
                "El salario base no puede ser negativo"
            )

        self._salario_base = valor


    @property
    def horas_extra(self):

        return self._horas_extra


    @horas_extra.setter
    def horas_extra(self, valor):

        if valor < 0:
            raise ValueError(
                "Las horas extra no pueden ser negativas"
            )

        self._horas_extra = valor


    @property
    def tarifa_extra(self):

        return self._tarifa_extra


    @tarifa_extra.setter
    def tarifa_extra(self, valor):

        if valor < 0:
            raise ValueError(
                "La tarifa extra no puede ser negativa"
            )

        self._tarifa_extra = valor


    @property
    def salario_total(self):

        return (
            self._salario_base
            + (
                self._horas_extra
                * self._tarifa_extra
            )
        )


emp = Empleado(
    "Laura Martínez",
    2000,
    10,
    15
)


print(f"Empleado: {emp.nombre}")
print(
    f"Salario base: "
    f"{emp.salario_base}€"
)
print(
    f"Horas extra: "
    f"{emp.horas_extra}"
)
print(
    f"Tarifa extra: "
    f"{emp.tarifa_extra}€/hora"
)
print(
    f"Salario total: "
    f"{emp.salario_total}€"
)


emp.horas_extra = 15
emp.tarifa_extra = 20


print(
    f"Nuevo salario total: "
    f"{emp.salario_total}€"
)