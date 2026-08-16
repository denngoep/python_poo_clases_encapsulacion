# Ejemplo 8: Acceso directo a atributos


class ConfiguracionSimple:

    def __init__(self):

        self.modo_debug = False
        self.max_conexiones = 100
        self.tiempo_espera = 30


configuracion = ConfiguracionSimple()


print(configuracion.modo_debug)
print(configuracion.max_conexiones)
print(configuracion.tiempo_espera)