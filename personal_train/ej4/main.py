# Hace rato no programaba asi que fui con un ejercicio un poco más facil xD

#  Crea un programa que modele un sistema básico de gestión de estudiantes con las siguientes características (las caracteristicas fueron proporsionadas por "chatGTP"):

class Estudiante():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    # funcion par agregar notas
    def agregar_nota(self,nota):
        self.notas.append(nota)
    
    def promedio(self):
        if self.notas == []:
            return 0
        else: 
            return sum(self.notas)/len(self.notas)
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}, Promedio: {self.promedio()}"
    
# Iteracion de la clase Estudiante

estudiante1 = Estudiante("Juan", 20)
estudiante1.agregar_nota(10)
estudiante1.agregar_nota(5)
estudiante1.agregar_nota(8)
print(estudiante1)

estudiante2 = Estudiante("Ana", 22)
estudiante2.agregar_nota(9)
estudiante2.agregar_nota(7)
estudiante2.agregar_nota(6)
print(estudiante2)

estudiante3 = Estudiante("Pedro", 21)
estudiante3.agregar_nota(10)
estudiante3.agregar_nota(10)
estudiante3.agregar_nota(10)
print(estudiante3)

estudienta4 = Estudiante("Amaro Gamín", 1)
estudienta4.agregar_nota(5.5)
estudienta4.agregar_nota(5.8)
estudienta4.agregar_nota(6.2)
print(estudienta4)