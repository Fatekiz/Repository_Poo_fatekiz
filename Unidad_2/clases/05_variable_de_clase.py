class CuentaBancaria:
    tasa_interes = 0.3 # <-- variable de clase, compartida para todas las instancias de la clase.

    def __init__(self,titular,saldo):
        self.titular = titular # Variable de instancia
        self.__saldo = saldo # Variable de instancia (privada)


    def calcular_interes(self):
        # Acceso a la variable de clase desde una instancia
        return self.__saldo * self.tasa_interes
    
print("Tasa de interés (Acceso desde la clase):", CuentaBancaria.tasa_interes)

# Crendo objetos
cuenta1 = CuentaBancaria("Benjamin Concha",5000)
cuenta2 = CuentaBancaria("Rocio cárdenas", 10000)

# Acceso a la variable desde una instancia
print("Tasa de interes (Acceso desde cuenta 1)",cuenta1.calcular_interes())
print("Tasa de interes (Acceso desde cuenta 2)",cuenta2.calcular_interes())

# Modificando variable de clase desde fuera
CuentaBancaria.tasa_interes = 0.3 # <-- para todas las instancias