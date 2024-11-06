"""
° La universidad ofrecerá descuentos en la cafetería para estudiantes y
académicos. Los estudiantes tienen un 20% de descuento y los
académicos un 10%. Si una persona no es estudiante ni académico, no
tiene descuento. 

° El sistema debe gestionar a los clientes, calcular el precio
final de su compra después de aplicar el descuento adecuado y registrar
las compras realizadas en la cafetería."""

class CafeteriaUniversidad():
    """ ## Variables de clase ##
    1. A. los defino como variables de clase 
    """
    desc_estudiantes = 0.2
    desc_académicos = 0.1

    """ ## Encapsulación y Atributos privados ##
    1. A.1) Creo que debe encapsularse el nombre el tipo y el total que pagaran cada uno ya que son datos que usaremos en funciones y dentro de la 'clase'
       A.2) Los atributos privados seran el nombre y el tipo para resguardar la informacion del cliente, el total a pagar sera publico para que pueda ser visible 
    """

    def __init__(self,nombre,tipo,total,compra):
        self.__nombre = nombre # nombre del cliente
        self.__tipo = tipo # el tipo del cliente 
        self.total = total # precio de la compra
        self.__descuento = 0 
        self.compra = compra
        assert self.__tipo == "estudiante" or  self.__tipo == "academico" or  self.__tipo == "otro" , "¡¡ Error: El tipo debe ser ('estudiante','academico','otro') !!" # <--- con este aserto puedo verificar que el tipo esta bien ingresado 
                                                                                                                                                                        #       y de esta manera puedo aplicar de manera correcta los descuentos """
        assert self.total > 0 , "¡¡ Error: El total a pagar no puede ser 0 o numeros negativos !!" # <-- así me aseguro de que el total a pagar no sean numeros negativos
        

    def descuento(self): # verificara que descuento le corresponde a cada uno
        assert self.__tipo == "estudiante" or  self.__tipo == "academico"

        if self.__tipo == "estudiante":
            self.__descuento += CafeteriaUniversidad.desc_estudiantes
            print(f"Usted es {self.__tipo} y su descuento es del 20%")

        elif self.__tipo == "academico":
            self.__descuento += CafeteriaUniversidad.desc_académicos
            print(f"Usted es {self.__tipo} y su descuento es del 10%")


    # ACCESORES Y MUTADORES 
    @property
    def total(self): # <--- aca hago un getter con poperty y puedo acceder al total sin descuento
        return self.__total
    
    
    @total.setter
    def total(self,nuevo_total):
        self.__total = nuevo_total # <-- de esta manera puedo modificar el total o precio de la compra sin afectar la logica del descuento

    
    # METODOS ESTATICOS B) no ocuparia metodo estatico ya que necesito acceder a los datos/ atributos de la clase.
    def precio_final(self):
        des = self.__descuento * self.__total
        final = self.total - des
        print(f"El precio final a pagar con su descuento es de: ${final} pesos")


    







# Instancias
cliente1 = CafeteriaUniversidad("Benjamin","estudiante",7000,"Sandiwch")
cliente2 = CafeteriaUniversidad("Victor","academico",10000,"sushi")
cliente3 = CafeteriaUniversidad("Rocio","otro",20000,"Pizza familiar XL")

#Verificacion de descuentos
cliente1.descuento()
cliente2.descuento()
#cliente3.descuento() <-- arrojara error por el assert de la linea 32.
print("Precio sin descuento: "+ cliente1.total)
cliente1.total = 6000
cliente1.precio_final()