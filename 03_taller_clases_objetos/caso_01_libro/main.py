# Taller: Clases y Objetos en Python
# Caso 1: Clase Libro
#
# Este programa crea una clase Libro para representar libros de una biblioteca.
# Permite consultar la información del libro, prestarlo y devolverlo.


class Libro:
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """

        # Atributos del objeto Libro.
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

        # Todos los libros comienzan disponibles para préstamo.
        self.disponible = True

    def prestar(self):
        # Verifica si el libro está disponible.
        if self.disponible:
            # Cambia su estado porque ahora está prestado.
            self.disponible = False
            return f'El libro "{self.titulo}" ha sido prestado.'

        # Si ya estaba prestado, informa que no está disponible.
        return f'El libro "{self.titulo}" no está disponible.'

    def devolver(self):
        # Verifica si el libro se encuentra prestado.
        if not self.disponible:
            # Cambia nuevamente su estado a disponible.
            self.disponible = True
            return f'El libro "{self.titulo}" ha sido devuelto.'

        # Si ya estaba disponible, informa que ya estaba en la biblioteca.
        return f'El libro "{self.titulo}" ya estaba disponible en la biblioteca.'

    def informacion(self):
        # Convierte el valor booleano de disponible en un texto más entendible.
        estado = "Disponible" if self.disponible else "Prestado"

        # Devuelve toda la información del libro.
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Páginas: {self.paginas}\n"
            f"Estado: {estado}"
        )


# Prueba de la clase Libro
def main():

    # Crear dos objetos libro diferentes.
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Mostrar información inicial de los libros.
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")

    # Prestar los libros.
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")

    # Intentar prestar un libro ya prestado.
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")

    # Mostrar información después del préstamo.
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")

    # Devolver un libro.
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")

    # Intentar devolver un libro ya disponible.
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")

    # Mostrar información final.
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()