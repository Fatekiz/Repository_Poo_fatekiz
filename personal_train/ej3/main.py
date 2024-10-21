# Crear una libreria 

#clase y constructor
class Libro():
    def __init__(self,titulo,autor,isbn,disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    # Métodos
    def __str__(self): # metodo mágico para especificaciones del libro
        return f" \n Especificaciones de Libro:\n  Titulo: {self.titulo} | Autor: {self.autor} | isbn (codigo único): {self.isbn} | Disponibilidad: {self.disponible} \n"
    
    def prestar(self,nombre,autor): # 2 parametros (para buscar el libro)
        if self.nombre == nombre and self.autor == autor: # si los parámetros de la clase con los del método coinciden entonces:
            if self.disponible == 'disponible': # y si el libro está disponible
                self.disponible = 'no disponible'  # cambiar disponibilidad
                print(f"El libro se ha prestado")
            else:
                print(f"El libro no está disponible para ser prestado.")
        else: # si los parámetros no coinciden, entonces informar que no existe el libro.
            print("El libro indicado no se encuentra.")
    
    def devolver(self,nombre,autor): # lo mismo pero al revez
        if self.nombre == nombre and self.autor == autor: # si los parámetros de la clase con los del método coinciden entonces:
            if self.disponible == 'no disponible': # y si el libro está disponible
                self.disponible = 'disponible'  # cambiar disponibilidad
                print(f"El libro se ha devuelto con éxito")
            else:
                print(f"El libro no se ha prestado.")
        else: # si los parámetros no coinciden, entonces informar que no existe el libro.
            print("El libro indicado no se encuentra.")

# Clase y constructor de | Biblioteca |
class Biblioteca():
    def __init__(self):
        self.libros = [] # lista vacía 


    def agregar_libros(self,libro):
        self.libros.append(libro)
        print(f"se ha agregado correctamente el libro {libro.titulo}")

    def buscar_libros(self,titulo):
        for i in self.libros:
            if i.titulo.lower() == titulo.lower():
                return i
        return None
    
    def mostrar_libreria(self):
        print("\nLibros en la libreria\n")
        for i in self.libros:
            print(f" Titulo: {i.titulo} | autor: {i.autor}")





# Creando objetos

libro = Libro("En el principio","Benjamin Concha", 1,"disponible")
libro2 = Libro("El bien y el mal","Desconocido", 2,"disponible")
libro3 = Libro("no mas que hacer","Benjamin Concha", 3,"disponible")

print(libro)
print(libro2)
print(libro3) 

# INSTANCIA PARA LA BIBLIOTECA

biblioteca = Biblioteca()

biblioteca.agregar_libros(libro)
biblioteca.agregar_libros(libro2)
biblioteca.agregar_libros(libro3)

buscando_libro = biblioteca.buscar_libros("en el principios") # falto hacer el print
if buscando_libro:
    print(buscando_libro)
else:
    print(f"el libro  no se encuentra en la biblioteca")

biblioteca.mostrar_libreria()

# <-- LISTO --> 