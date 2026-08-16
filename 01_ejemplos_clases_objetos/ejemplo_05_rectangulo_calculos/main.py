# Ejemplo 5: Inicialización de atributos con cálculos
# Tema: Clases, objetos y constructor __init__

# Se crea la clase Rectangulo.
class Rectangulo:

    # El constructor recibe el ancho y el alto del rectángulo.
    def __init__(self, ancho, alto):

      # Se guardan el ancho y el alto como atributos del objeto.
        self.ancho = ancho
        self.alto = alto

  # El constructor también puede realizar cálculos.
        # Se calcula el área multiplicando el ancho por el alto.
        self.area = ancho * alto 

          # Se calcula el perímetro sumando ancho y alto
        # y multiplicando el resultado por 2.
        self.perimetro = 2 * (ancho + alto)


# Creamos un objeto de la clase Rectangulo.
# El rectángulo tendrá 5 de ancho y 3 de alto.
rect = Rectangulo(5, 3)

# Mostramos los atributos calculados.
print("Ancho:", rect.ancho)
print("Alto:", rect.alto)
print("Área:", rect.area)
print("Perímetro:", rect.perimetro)
