import math
# Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas
# Propiedades a la clase Persona:
class Persona():

    # Constructor de clase
    def __init__(self, nombre, apellido, edad,altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)


    # Atributos de clase (Características compartidas por todos los objetos de la clase)
    # nombre = "Cristina"
    # apellido = "Torres"
    # edad = 23   

    #Métodos (Comportamientos) (Deben estar dentro de la clase)
    def hablar(self):
        print(f"{self.nombre} está hablando")

    def caminar(self):
        print(f"{self.nombre} está caminando")

    def calcular_imc(self): 
        imc = (self.peso / (self.altura**2))

        if imc < 18.5:
            print(f" Según su imc se encuentra con un peso insuficiente.")
        elif imc >= 18.5 and imc < 25:
            print(f" Según su imc se encuentra con un peso ideal y dentro del rango saludable.")    
        else:
            print("Según su imc se encuentra  ")





    
# Creacion de un objeto de la clase  Persona / Instanciando clase

persona1 = Persona("Rocio", "Cardenas", 27, 1.53, 65)
persona2 = Persona("Benjamin", "Concha", 19, 1.71, 100)

# imprimiendo 
