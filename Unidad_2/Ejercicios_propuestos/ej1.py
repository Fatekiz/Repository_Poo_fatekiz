# clase para el vehiculo
class Vehiculo():
    def __init__(self,marca,modelo,año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True

    def marcar_vendido(self):
        self.__disponible = False

    def __str__(self):
        return f"\n Especifaciones del vehículo:\n Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__año} | Disponibilidad: {self.__disponible} \n"
    

class Consecionaria():
    def __init__(self):
        self.stock = []

    def agregar_vehiculo(self,marca,modelo,año,disponible):
        vehiculo = {
            'marca' : marca,
            'modelo' : modelo,
            'año' : año,
            'disponible' : disponible
        }
        self.stock.append(vehiculo)

    def mostrar_vehiculos(self):

        for vehiculo in self.stock:
            disponible_texto = "El vehículo está disponible" if vehiculo['disponible'] else "El vehículo NO está disponible"
            print(f" \n Vehiculos Disponibles\n Marca: {vehiculo['marca']} | modelo: {vehiculo['modelo']} | año: {vehiculo['año']} | disponible: {disponible_texto} ")
    
    def vender_vehiculo(self,marca,modelo):
        for vehiculo in self.stock:
            if vehiculo['marca'] == marca and vehiculo['modelo'] == modelo:
                if vehiculo['disponible']:
                    vehiculo['disponible'] = False
                    print(f"El vehiculo {marca} {modelo} ha sido vendido.")
                    return
                else:
                    print(f"El vehiculo de {marca} {modelo} ya está vendido")
                    return
        print(f"El vehiculo {marca} {modelo} no se encuentra en el stock.")



#############################################################
# creando objetos en la clase vehiculo
auto1 = Vehiculo("Peugeot", "208", "2019")
auto2 = Vehiculo("Hyundai","Santa Fe","2010")


print(auto1) #espicificaciones
print(auto2)

auto1.marcar_vendido() #vendiendo auto
print(auto1)

# creando objetos en la consecionaria

berrios = Consecionaria()
berrios.agregar_vehiculo("Peugeot","208","2019",True)
berrios.agregar_vehiculo("Renault","Kwaii","2024",True)
berrios.agregar_vehiculo("kia","Rio 5", "2022", True)
berrios.mostrar_vehiculos()

berrios.vender_vehiculo("Peugeot","208") # avisará que se vendió el vehiculo

berrios.mostrar_vehiculos()