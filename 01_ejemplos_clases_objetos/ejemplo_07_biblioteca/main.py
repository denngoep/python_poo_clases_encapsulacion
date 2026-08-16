# Ejemplo 7: Modelando una biblioteca
# Tema: Clases, objetos y constructor __init__

# Se crea la clase Libro.
class Libro:

 # El constructor recibe los datos principales del libro.
    # disponible tiene True como valor predeterminado.
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):

          # Se almacenan los datos recibidos como atributos del objeto.
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible

        # Todos los libros comienzan en la página 0.
        self.pagina_actual = 0

# Creamos el primer libro.
# Como no indicamos el valor de disponible,
# automáticamente será True.
libro1 = Libro(
    "Python Crash Course",
    "Eric Matthes",
    544,
    "9781593279288"
)

# Creamos un segundo libro.
# En este caso indicamos False,
# lo que significa que el libro está prestado.
libro2 = Libro(
    "Clean Code",
    "Robert C. Martin",
    464,
    "9780132350884",
    False
)

# Mostramos el estado de disponibilidad de cada libro.
print(
    f"{libro1.titulo} está "
    f"{'disponible' if libro1.disponible else 'prestado'}"
)

print(
    f"{libro2.titulo} está "
    f"{'disponible' if libro2.disponible else 'prestado'}"
)