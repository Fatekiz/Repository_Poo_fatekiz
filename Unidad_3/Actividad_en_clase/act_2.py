# Crear un sistema para un juego con vehiculos, donde comparten comportamientos y caract. pero también combinar  atributos como de terrestres, acua. o aereos
# Usar herencia multiple para vehiculos hibridos y polimorfismo para manejar diferentes tipos de vehiculos de manera uniforme.

# Clase madre
class Vehiculo():
    def __init__(self,velocidad,gasolina,color,marca):
        self.velocidad = velocidad
        self.color = color
        self.marca = marca 
        self.gasolina = gasolina

    def carrera(self):
        assert self.gasolina > 0, "El vehiculo no tiene gasolina para correr"
        print("El vehiculo dispone de gasolina, por lo cuál puede participar en una carrera")
        print(f"Y corre con una velocidad de: {self.velocidad}km/h")

#clases hijas:

class Auto(Vehiculo):
    def __init__(self, velocidad, gasolina, color, marca,ruedas):
        super().__init__(velocidad, gasolina, color, marca)
        self.ruedas = ruedas


    def activar4x4(self):
        assert self.ruedas == True, "Error, el vehiculo debe tener ruedas para activar el 4x4"
        print("El auto ha activado el 4x4")

    def frenar_poco(self):
        self.velocidad = self.velocidad -5
        print(f"el vehiculo disminuyó su velocidad, y ahora su velocidad es de {self.velocidad}")


class Barco(Vehiculo):
    def __init__(self, velocidad, gasolina, color, marca, vela):
        super().__init__(velocidad, gasolina, color, marca)
        self.vela = vela

    def desplegar_vela(self):
        assert self.vela == True
        print("El barco ha desplegado la vela")


# Creación de loss objetos
auto1 = Auto(100,30,"Azul","Peugeot",True)
barco1 = Barco(80,10,"Café","N/A",True)

# ocupando los métodos

auto1.activar4x4()
auto1.frenar_poco()

barco1.carrera()
barco1.desplegar_vela()