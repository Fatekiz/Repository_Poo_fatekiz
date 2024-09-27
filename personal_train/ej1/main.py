# crear una tienda de música

class Tienda(): # Clase
    def __init__(self,nombre,artista,genero,precio,disponibles): # constructor
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.precio = precio
        self.disponibles = disponibles
        self.stock = [] #lista vacia donde se almacenaran las canciones
        # Métodos
    
    def agregar_cancion(self): # método para agregar alguna cancion
        cancion = {
            "nombre" : self.nombre,
            "artista" : self.artista,
            "genero" : self.genero,
            "precio" : self.precio,
            "disponibles" : self.disponibles
        }
        self.stock.append(cancion)
        print(f"Se ha agregado exitosamente la cancion {cancion['nombre']} de {cancion['artista']} con una disponibilidad de {cancion['disponibles']}.")

    def mostrar_cancion(self):
        if not self.stock:
            print(f"No hay canciones en stock para la venta.")
        else:
            print("Canciones disponibles en stock")
            for cancion in self.stock:
                print(f"nombre: {cancion['nombre']}, artista: {cancion['artista']}, genero: {cancion['genero']}, valor: ${cancion['precio']}, disponibles: {cancion['disponibles']}\n ")

# Instanciar
cancion1 = Tienda("Paz","Álvaro López", "Pop", 2000, 100)
cancion2 = Tienda("Hoy te puedo sentir","Álvaro López", "Pop", 1500, 50)

cancion1.agregar_cancion()

cancion1.mostrar_cancion()
cancion2.mostrar_cancion()

cancion2.agregar_cancion()
cancion2.mostrar_cancion()