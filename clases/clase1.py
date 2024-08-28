# Creando clase

# Una clase contiene Atributos y Métodos

class Persona():

    # Constructor de clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Atributos de clase (Características compartidas por todos los objetos de la clase)
   # nombre = "Cristina"
   # apellido = "Torres"
   # edad = 23   

    #Métodos (Comportamientos) (Deben estar dentro de la clase)
    def hablar(self):
        print(f"{self.nombre} está hablando")

    def caminar(self):
        print(f"{self.nombre} está caminando")

    
# Creacion de un objeto de la clase  Persona / Instanciando clase

persona1 = Persona("Rocio", "Cardenas", 27)
persona2 = Persona("Benjamin", "Concha", 19)

# Acceso a  los atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")

# LLamando metodos
persona1.hablar()
persona2.caminar()