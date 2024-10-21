# Cafetería de gatos 

# Peticiones Gatos en café:

# 1) LISTA
# ....
# 2) LISTA
# a. ¿Cómo diseñarías un método que permita que los gatos jueguen y cómo impactaría esto en sus niveles de energía y hambre?
# b. ¿Cómo diseñarías un método que permita alimentar a los gatos y restaurar sus niveles de energía?
# 3) LISTA
# a. Implementa un método que te permita imprimir de forma clara el estado del gato. ¿Qué información incluirías en la representación del gato?

# me aburri de seguir por tiempo :c


class Gato(): #Clase para la creaciones de los gatos
    def __init__(self,nombre,color,color_ojos,energia,hambre):
        self.__nombre = nombre
        self.__color = color
        self.__color_ojos = color_ojos
        self.energia = energia
        self.hambre = hambre
    
    def jugar(self,accion): # Para jugar con los gatos | LISTO
        if self.energia <= 0 or self.hambre <= 0:
            print("El gato no tiene suficiente energía o hambre para poder jugar contigo. Alimentalo o dejalo descasar! (verifica su estado)")
        else:
            print(f"Jugarás con el/la gato(a): {self.__nombre} | En este momento: Energía = {self.energia} Hambre = {self.hambre} ")
            if accion == "rodar":
                print(f"\n Hiciste que el(la) gato(a) {self.__nombre} ruede en el piso \n")
                self.energia = self.energia - 25 
                self.hambre = self.hambre - 40
            if accion == "saltar":
                print(f"\n ¡Hiciste que el gato {self.__nombre} saltara hasta tu altura! \n")
                self.energia = self.energia - 50
                self.hambre = self.hambre - 25

    def alimentar(self): # para alimentar el gato | LISTO
        print(f"\n ¡Bien, alimentaste al(la) gato(a) {self.__nombre} !\n")
        self.hambre = self.hambre + 70

    def descansar(self): # para hacer descansar el gato  | LISTO
        print(f"El(la) gato(a) {self.__nombre} se sentó en tus piernas, le hiciste cariño y ahora está descansando")
        self.energia = self.energia + 50


    def __str__(self): # para mostrar la información del gato
        return f"\n Información Completa y actual del gato:\n | Nombre: {self.__nombre} |\n | Color del gato: {self.__color} |\n | Color de ojos del gato: {self.__color_ojos} |\n | energia: {self.energia} |\n | hambre: {self.hambre} |\n  "


class Area():
    def __init__(self,nombre,id,capacidad):
        self.__nombreArea = nombre
        self.__id = id
        self.__capacidad = capacidad
        self.lista = []
    
    # agregar gatos al area
    def agregar(self,gato):
        if len(self.lista) >= self.__capacidad:
            print(f"\nel Area {self.__nombreArea} no tiene más capacidad para gatos, la capacidad total es de: {self.__capacidad}")
        else:
            self.lista.append(gato)
            print(f" ¡El gato con la información {gato} ha sido ingresado correctamente! Al área '{self.__nombreArea}'")
            print(f" \nAhora la cantidad de gatos en el area es de {len(self.lista)}")

    def mostrar_cantidad(self):
        if self.lista:
            for i in self.lista:
                print(f"\nInformaciones de todos los gatos presentes en el área {self.__nombreArea}\n") 
                print(f" {i}")


class Inventario():
    def __init__(self,alimentos,juguetes):
        self.alimentos = alimentos
        self.juguetes = juguetes
        cantidadjuguetes = []







#...................................................

# CREACIONES DE LOS GATOS

gato1 = Gato("Benja","Negro","Marrones",100,50)
gato2 = Gato("Rocio","Blanco","Verdes",50,100)
gato3 = Gato("Cristian","amarillo","azules",75,75)
gato4 = Gato("Liam","negro","Verdes",75,100)
gato5 = Gato("Zayn","plomo","gris",99,75)

#CREACIONES DE AREAS
area1 = Area("Recepcion",3354,2)
area2 = Area("Comedor",3354,3)




#..........................................
# MOSTRANDO LAS INFOS DE LOS GATOS
print(gato1)
print(gato2)
print(gato3)
print(gato4)
print(gato5)

# JUGANDO CON GATOS
gato1.jugar("rodar")
gato1.jugar("saltar")
gato2.jugar("saltar")
gato1.jugar("rodar") # aca no hay suficiente energía para poder jugar con el gato y nos mostrará la advertencia
print(gato1) # imprimiendo info
gato1.alimentar()
gato1.descansar() #alimentandolos y haciendolos descansar 
gato1.jugar("rodar") # volviendo a jugar

# INGRESANDO GATOS A LAS AREAS
area1.agregar(gato1)
area1.agregar(gato2)
area1.agregar(gato3) # me excedo de gatos (2 máx)
area2.agregar(gato3) # ahora si cristian xdd
area2.agregar(gato4)
area2.agregar(gato5)

area1.mostrar_cantidad()
area2.mostrar_cantidad()