class CuentaBancaria:
    def __init__(self,titular,efectivo,saldo):
        self.titular = titular
        self.__saldo = saldo
        self.efectivo = efectivo
        # Aserción para asegurar la invariante en la inicializacón del objeto (no iniciar el saldo en -1 hacia abajo)
        assert self.__saldo >= 0, "Error: El saldo no puede ser negativo" # Dará un error si la cuenta se inicia incumpliendo este 'assert'

    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,new_saldo):
        if new_saldo >= 0:
            self.__saldo = new_saldo
        else:
            print("Error: El nuevo saldo no puede ser negativo")
    
    def depositarse(self,monto):
        # precondicion
        assert monto <= 0, "Error: El monto a depositar no puede ser 0 o un monto en negativo."
        self.__saldo += monto
    

    def retirar(self,monto):
        assert monto > self.__saldo, "Error: El monto a retirar no puede ser mayor al saldo disponible"
        self.saldo -= monto
        self.efectivo += monto

    def info(self):
        print(f"la cuenta de {self.titular} tiene: ${self.__saldo}")

C_falabella = CuentaBancaria("Benja",30000)
C_falabella.saldo = 29000
C_falabella.info()