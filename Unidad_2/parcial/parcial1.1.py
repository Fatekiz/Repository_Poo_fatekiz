# Este código lo voy avanzando a medida que tengo tiempo


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
    
    def newJugar(self,accion,juguete): # Para newJugar con los gatos | LISTO


        if self.energia <= 0 or self.hambre <= 0:
            print("El gato no tiene suficiente energía o hambre para poder newJugar contigo. Alimentalo o dejalo descasar! (verifica su estado)")
        else:
            print(f"Jugarás con el/la gato(a): {self.__nombre} | En este momento: Energía = {self.energia} Hambre = {self.hambre} ")
            if accion == "rodar":                                                                                              # <-- se debe jugar con el segundo argumento "nada"
                if juguete == "nada":
                    print(f"\n Hiciste que el(la) gato(a) {self.__nombre} ruede en el piso \n")
                    self.energia = self.energia - 25 
                    self.hambre = self.hambre - 40
            if accion == "saltar":                                 #                                              <--- se debe jugar con el segundo argumento "pelota"
                if juguete == pelota:
                    if juguete.cantidad >= 1:
                        
                        print(f"\n ¡Hiciste que el gato {self.__nombre} saltara hasta tu altura! \n")
                        self.energia = self.energia - 50
                        self.hambre = self.hambre - 25
                        juguete.cantidad -=1
                    else:
                        print("No se encuentra disponible el juguete seleccionado, cambielo o reponga su cantidad en el stock")
                else:
                    print("No se encuentra en el stock de juguetes el juguete seleccionado por usted.")
            else:
                print("No puede realizar esa acción con el gato")


    def newAlimentar(self,producto): # funcion para alimentar segun inventario exitosa!
        if producto == salmon:
            if producto.cantidad >= 1:
                self.hambre = self.hambre + 70 # se incrementa el nvl de hambre
                producto.cantidad -= 1 # se resta uno
                print(f"\n ¡Bien, alimentaste al(la) gato(a) {self.__nombre} !\n")
            else: 
                print(f"El alimento: '{producto.nombre}' no tiene stock, ¡se debe rellenar!")
        else:
            print("No esta dispopnible el alimento que usted indicó.")
            
        
        
        

    def descansar(self): # para hacer descansar el gato  | LISTO
        print(f"El(la) gato(a) {self.__nombre} se sentó en tus piernas, le hiciste cariño y ahora está descansando")
        self.energia = self.energia + 50


    def __str__(self): # método mágico para mostrar la información del gato.
        e_hambre = ""
        e_energia = ""
        if self.hambre > 0:
            e_hambre = "Sin hambre"
        elif self.hambre <= 0:
            e_hambre = "Hambriento"
        if self.energia > 0: 
            e_energia = "El gato se encuentra con energía"
        elif self.energia <= 0:
            e_energia = "El gato no tiene suficiente energía"
        return f"\n Información Completa y actual del gato:\n | Nombre: {self.__nombre} |\n | Color del gato: {self.__color} |\n | Color de ojos del gato: {self.__color_ojos} |\n | energia: {self.energia} | estado de energia {e_energia} | \n | hambre: {self.hambre} | estado de hambre: {e_hambre}  \n  "
    
    def get_nombre(self):  
        return self.__nombre        # <--- con este método publico podria acceder a los nombres aunque sean privados. (pero solo con esta manera) 


class Area():
    def __init__(self,nombre,id,capacidad):
        self.__nombreArea = nombre
        self.__id = id
        self.__capacidad = capacidad              # <-- LISTA
        self.lista = []
    
    # agregar gatos al areaA
    def agregar(self,gato):
        if len(self.lista) >= self.__capacidad:
            print(f"\n No se pudo ingresar el gato '{gato.get_nombre()}' | El Area '{self.__nombreArea}' no tiene más capacidad para gatos, la capacidad total es de: {self.__capacidad}\n")
        else:
            self.lista.append(gato)
            print(f"¡El gato {gato.get_nombre()} ha sido agregado a la lista exitosamente!")
            print(f" Ahora la cantidad de gatos en el area '{self.__nombreArea}' es de {len(self.lista)}. (Recuerda que el máximo de gatos en este área es de {self.__capacidad}) \n")

    def mostrar_cantidad(self):
        if self.lista:
            print(f"\n Gatos del área '{self.__nombreArea}' \n")      # <--- LISTO
            for i in self.lista:
                print(i.get_nombre())
        else:
            print(f"No hay gatos en el Área '{self.__nombreArea}' ")
            
#Clase para los productos
class Producto():
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad # inicial de cada producto
        self.stock = []

    def agregar(self,producto):
        self.stock.append(producto) 
        print(f"Se ha agregado tu producto {producto.nombre}")

    def restaurar(self,producto,cantidad):
        if producto == salmon:
            self.cantidad += cantidad
    





#...................................................

# CREACIONES DE LOS GATOS

gato1 = Gato("Benja","Negro","Marrones",100,50)
gato2 = Gato("Rocio","Blanco","Verdes",50,100)
gato3 = Gato("Cristian","amarillo","azules",75,75)
gato4 = Gato("Liam","negro","Verdes",75,100)
gato5 = Gato("Zayn","plomo","gris",99,75)

# CREACIONES DE AREAS
area1 = Area("Recepcion",3354,2)
area2 = Area("Comedor",3354,3)

# CREANDO LOS PRODUCTOS
pelota = Producto("pelota",2)
salmon = Producto("salmon",1)



#....................................................
# MOSTRANDO LAS INFOS DE LOS GATOS
print(gato1)
print(gato2)
print(gato3)
print(gato4)
print(gato5)

# JUGANDO CON GATOS
gato1.newJugar("rodar","nada")
gato1.newJugar("saltar",pelota)
gato2.newJugar("saltar",pelota)
gato1.newJugar("rodar","nada") # aca no hay suficiente energía para poder newJugar con el gato y nos mostrará la advertencia
print(gato1) # imprimiendo info
gato1.newAlimentar(salmon)
gato1.newAlimentar(salmon)
salmon.restaurar(salmon,2)
gato1.newAlimentar(salmon)
#gato1.alimentar()
gato1.descansar() #alimentandolos y haciendolos descansar 
gato1.newJugar("rodar","nada") # volviendo a newJugar

# INGRESANDO GATOS A LAS AREAS
area1.agregar(gato1)
area1.agregar(gato2)
area1.agregar(gato3) # me excedo de gatos (2 máx)
area2.agregar(gato3) # ahora si cristian xdd
area2.agregar(gato4)
area2.agregar(gato5)

# MOSTRANDO LAS CANTIDADES DE GATOS EN CADA ARENA
area1.mostrar_cantidad()
area2.mostrar_cantidad()

#                                   EJERCICIO TERMINADO EN 190 lineas de código :| , gracias profe me ayudo xd :D