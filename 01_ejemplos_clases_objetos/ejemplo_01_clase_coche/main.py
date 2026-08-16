# Ejemplo 1: Creación de una clase básica
# Tema: Clases y objetos

#  Se define una clase llamada Coche. 
# Una clase funciona como una plantilla o plano 
# para poestriormente crear objetos.

class Coche:

    # La palabra pass indica que la clase está vacía por ahora. 
    # Python permite crearla aunque todavía no tenga atributos ni métodos.

    pass

# Creamos un objetos llamado mi_coche
# utilizando como plantilla la clase de Coche. 

mi_coche = Coche()

# Creamos otro objeto llamado coche_de_amigo.
# Este es un objeto diferente, aunque utiliza  la misma clase Coche. 

coche_de_amigo = Coche()

# Mostramo los objetos creados en la consola.
print("Objeto mi_coche:", mi_coche)
print("Objeto coche_de_amigo:", coche_de_amigo)
