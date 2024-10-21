# tienda de canciones que se puedan pasar canciones desde el inicio

class Tienda():
    def __init__(self,canciones=None):
        self.stock = canciones if canciones is not None else [] # si no se inicia con canciones se inicia el stock con la lista de canciones / o vacio si no se pasa nada

    # metodo para agregar las canciones
    def agregar_canciones(self,nombre,artista,genero,precio,disponible):
        cancion = {
            'nombre' : nombre,
            'artista' : artista,
            'genero' : genero,
            'precio' : precio,
            'disponible' : disponible,
        }
        self.stock.append(cancion)
        print(f"La cancion {cancion['nombre']} de {cancion['artista']} se ha agregado correctamente.")
    
    def mostrar_stock(self):
        if not self.stock:
            print(f"No hay canciones disponibles en el stock")
        else:
            print(f"Canciones disponibles")
            for cancion in self.stock:
                print(f" {cancion['nombre']} - {cancion['artista']} - {cancion['genero']} - ${cancion['precio']} - unidades: {cancion['disponible']} ") # debo usar comillas simples
        
    def modificar_stock(self,nombre,new_name):
        for nombre in self.stock:
            if nombre == self.stock["nombre"]:
                self.stock["nombre"] = new_name
                print("Se ha cambiado correctamente el nombre a la cación ")


canciones_iniciales = [
    {'nombre': 'Un milagro hay para ti', 'artista': 'Coros Unidos', 'genero': 'Alabanza', 'precio': 0, 'disponible': 500},
    {'nombre': 'Uno más grande que el templo', 'artista': 'Coros Unidos', 'genero': 'Alabanza', 'precio': 0, 'disponible': 1500},
    {'nombre': 'Cancion favorita', 'artista': 'Coros Metropolitano', 'genero': 'Alabanza', 'precio': 2000, 'disponible': 2500}

]

# iniciando tienda
tienda = Tienda(canciones=canciones_iniciales)

tienda.mostrar_stock()

tienda.agregar_canciones("Lucas 13", "Benta", "Alabanza", 0, 100)

tienda.mostrar_stock()

tienda.modificar_stock("Lucas 13", "Lucas-13")

# <-- En proceso -->