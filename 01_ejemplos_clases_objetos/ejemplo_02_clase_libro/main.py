# Ejemplo 2: Clase Libro
# Tema: Clases y objetos

# Se define una clase llamada Libro.
# Esta clase funciona como una plantilla para crear objetos de tipo Libro.
class Libro:

    # Por ahora la clase está vacía.
    # Más adelante se agregarán atributos como:
    # titulo, autor y paginas.
    #
    # También se podrán agregar métodos como:
    # abrir(), leer() y cerrar().
    pass


# Creamos un objeto llamado libro_python
# utilizando como plantilla la clase Libro.
libro_python = Libro()


# Creamos otro objeto llamado novela_fantasia.
# Aunque utiliza la misma clase Libro,
# es un objeto diferente.
novela_fantasia = Libro()


# Mostramos los objetos creados.
print("Objeto libro_python:", libro_python)
print("Objeto novela_fantasia:", novela_fantasia)