# Ejemplo 16: Procesamiento de datos
# utilizando métodos privados


class ProcesadorTexto:

    def __init__(self):

        self._texto = ""
        self._estadisticas = {}


    def procesar_archivo(
        self,
        ruta_archivo
    ):

        try:

            texto = self.__leer_archivo(
                ruta_archivo
            )

            self._texto = (
                self.__normalizar_texto(
                    texto
                )
            )

            self._estadisticas = (
                self.__calcular_estadisticas(
                    self._texto
                )
            )

            return True


        except Exception as e:

            print(
                f"Error al procesar "
                f"el archivo: {e}"
            )

            return False


    def __leer_archivo(self, ruta):

        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as archivo:

            return archivo.read()


    def __normalizar_texto(
        self,
        texto
    ):

        texto = texto.lower()

        import re

        texto = re.sub(
            r"[^\w\s]",
            "",
            texto
        )

        texto = re.sub(
            r"\s+",
            " ",
            texto
        ).strip()

        return texto


    def __calcular_estadisticas(
        self,
        texto
    ):

        palabras = texto.split()

        estadisticas = {

            "total_palabras":
                len(palabras),

            "palabras_unicas":
                len(set(palabras)),

            "longitud_promedio":
                sum(
                    len(p)
                    for p in palabras
                ) / len(palabras)
                if palabras
                else 0
        }

        return estadisticas


    def obtener_estadisticas(self):

        return self._estadisticas.copy()


    def obtener_texto_procesado(self):

        return self._texto


procesador = ProcesadorTexto()


if procesador.procesar_archivo(
    "02_ejemplos_encapsulacion/"
    "ejemplo_16_procesador_texto/"
    "texto.txt"
):

    print(
        procesador.obtener_texto_procesado()
    )

    print(
        procesador.obtener_estadisticas()
    )