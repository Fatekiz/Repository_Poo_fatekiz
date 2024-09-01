# Creando una clase 

class Coche():


    # constructor de la clase
    def __init__(self,marca,gasolina):
        self.marca = marca
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = 0.0

    # Metodo para conducir
    def conducir(self,kilometros):
        gasolina_necesaria = kilometros /10  # por 1 litro de bencina recorre 10 km
        if self.gasolina >= gasolina_necesaria:
            self.kilometros_recorridos += kilometros
            self.gasolina -= gasolina_necesaria
            print(f"Has conducido {kilometros} kilómetros. Gasolina restante {self.gasolina:.2f} Litros")
        
        else:
            kilometros_posibles = self.gasolina * 10 # la cantidad posible que puede recorrer con la gasolina disponible
            self.kilometros_recorridos += kilometros_posibles
            self.gasolina = 0
            print(f"Solo pudiste conducir {kilometros_posibles:.2f} kilómetros y te has quedado sin gasolina")
        
    # Método para cargar gasolina
    def cargar_gasolina(self,litros):
        self.gasolina += litros
        print(f"Has cargado {litros} Litros de gasolina. gasolina actual: {self.gasolina:.2f} Litros")

# Crear instancias de la clase coche
coche1 = Coche("Peugeot", 10)
coche2= Coche("Lamborghini", 5)

# Método de conducir()
coche1.conducir(50)
coche1.conducir(100)

coche2.conducir(60)
coche2.cargar_gasolina(1) # le cargue 1km
coche2.conducir(10) # recorrio los 10 km restantes.

# Terminados, pude entender poco el tema de las funciones y la lógica matematica me costó