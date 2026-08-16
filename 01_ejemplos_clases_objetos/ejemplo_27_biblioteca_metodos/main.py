# Ejemplo 27: Biblioteca
# Integración de clases, atributos y métodos


class Libro:

    def __init__(self, titulo, autor, paginas):

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

        # El libro comienza en la página cero.
        self.pagina_actual = 0

        # El libro comienza cerrado.
        self.abierto = False


    # Abre el libro.
    def abrir(self):

        if self.abierto:
            return f"{self.titulo} ya está abierto"

        self.abierto = True

        return f"{self.titulo} ha sido abierto"


    # Cierra el libro.
    def cerrar(self):

        if not self.abierto:
            return f"{self.titulo} ya está cerrado"

        self.abierto = False

        return f"{self.titulo} ha sido cerrado"


    # Permite avanzar determinadas páginas.
    def leer(self, num_paginas):

        if not self.abierto:
            return (
                f"No puedes leer: "
                f"{self.titulo} está cerrado"
            )

        if self.pagina_actual >= self.paginas:
            return (
                f"Ya has terminado de leer "
                f"{self.titulo}"
            )

        paginas_restantes = (
            self.paginas - self.pagina_actual
        )

        paginas_a_leer = min(
            num_paginas,
            paginas_restantes
        )

        self.pagina_actual += paginas_a_leer


        if self.pagina_actual >= self.paginas:

            return (
                f"Has leído {paginas_a_leer} páginas "
                f"y has terminado {self.titulo}"
            )


        return (
            f"Has leído {paginas_a_leer} páginas. "
            f"Estás en la página "
            f"{self.pagina_actual} de {self.paginas}"
        )


    # Reinicia la lectura.
    def reiniciar_lectura(self):

        self.pagina_actual = 0

        return (
            f"Has reiniciado la lectura "
            f"de {self.titulo}"
        )


    # Define cómo se mostrará el objeto
    # cuando utilizamos print().
    def __str__(self):

        estado = (
            "abierto"
            if self.abierto
            else "cerrado"
        )

        progreso = (
            f"{self.pagina_actual}/"
            f"{self.paginas} páginas"
        )

        return (
            f"{self.titulo} por {self.autor} - "
            f"{progreso} - {estado}"
        )


# Creamos un libro.
libro = Libro(
    "El Quijote",
    "Miguel de Cervantes",
    863
)


# Probamos sus métodos.
print(libro.leer(50))
print(libro.abrir())
print(libro.leer(50))
print(libro.leer(100))
print(libro.cerrar())
print(libro.abrir())
print(libro.leer(713))
print(libro.reiniciar_lectura())
print(libro)