# Ejemplo 8: Constructores alternativos con métodos de clase
# Tema: Clases, objetos y @classmethod


# Se crea la clase Fecha.
class Fecha:

    # Constructor normal de la clase.
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio


    # @classmethod permite crear un método
    # que recibe la clase como primer parámetro.
    @classmethod
    def desde_texto(cls, texto):

        # Se separa el texto usando el guion como separador.
        # map(int, ...) convierte cada parte en número entero.
        dia, mes, anio = map(int, texto.split("-"))

        # Se crea y devuelve un nuevo objeto Fecha.
        return cls(dia, mes, anio)


    # Otro constructor alternativo.
    @classmethod
    def hoy(cls):

        # Se importa datetime para obtener la fecha actual.
        import datetime

        # Se obtiene la fecha actual del sistema.
        fecha_actual = datetime.date.today()

        # Se crea un objeto Fecha con los valores actuales.
        return cls(
            fecha_actual.day,
            fecha_actual.month,
            fecha_actual.year
        )


# Creamos una fecha usando el constructor normal.
fecha1 = Fecha(15, 3, 2023)

# Creamos una fecha desde un texto.
fecha2 = Fecha.desde_texto("25-12-2023")

# Creamos una fecha usando la fecha actual del computador.
fecha3 = Fecha.hoy()


# Mostramos las fechas.
print(f"Fecha 1: {fecha1.dia}/{fecha1.mes}/{fecha1.anio}")
print(f"Fecha 2: {fecha2.dia}/{fecha2.mes}/{fecha2.anio}")
print(f"Fecha actual: {fecha3.dia}/{fecha3.mes}/{fecha3.anio}")