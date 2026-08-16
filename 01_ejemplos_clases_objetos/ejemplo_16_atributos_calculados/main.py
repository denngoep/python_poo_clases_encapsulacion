# Ejemplo 16: Atributos calculados
# Tema: Propiedades


class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto


    # El área se calcula cada vez que
    # accedemos a esta propiedad.
    @property
    def area(self):
        return self.ancho * self.alto


    # El perímetro también se calcula dinámicamente.
    @property
    def perimetro(self):
        return 2 * (self.ancho + self.alto)


# Creamos el rectángulo.
rect = Rectangulo(5, 3)


print(f"Área: {rect.area}")
print(f"Perímetro: {rect.perimetro}")


# Modificamos el ancho.
rect.ancho = 7


# El área se actualiza automáticamente.
print(f"Nueva área: {rect.area}")