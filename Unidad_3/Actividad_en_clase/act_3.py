
"""
Una empresa está intentando desarrollar un sistema de gestión de pagos, admite diferentes tipos de pago:
- Tarjetas de crédito (la tarjeta debe ser validada previamente)
- Transferencias bancarias (necesitan un código de confirmación)
- Pago en efectivo (NO NECESITA SER VALIDADA)

* La clase base " MetodoDePago()" contiene el método "procesar_pago()" que asume que todos los métodos se deben validar previamente
    - Este método causa problema ya que los pagos en efectivos no necesitan validación.

- Solución a realizar: rediseñar la jerarquía de clases para que los métodos de pago cumplan
con el LSP, asegurando que las subclases puedan ser utilizadas de forma
intercambiable sin romper el programa.
    

"""

from abc import ABC, abstractmethod

# Clase base para todos los métodos de pago
class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

# Interfaz para métodos que necesitan validación
class Metodovalidable(ABC):
    @abstractmethod
    def validar(self):
        pass

# Pago con tarjeta de crédito
class TarjetaDeCredito(MetodoDePago, Metodovalidable):
    def __init__(self,numero_tarjeta, cvv):
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv
        self.validada = False

    def validar(self):
        # lógica de la validación
        print(f"Validando tarjeta {self.numero_tarjeta}...")
        self.validada = True

    def procesar_pago(self, monto):
        if not self.validada:
            raise Exception("La tarjeta no ha sido validada")
        print(f"Procesando pago de {monto} con trajeta de crédito.")


# Pago con transferencia bancaria
class TransferenciaBancaria(MetodoDePago, Metodovalidable):
    def __init__(self, codigo_confirmacion):
        self.codigo_confirmacion = codigo_confirmacion
        self.validada = False

    def validar(self):
        # logica de la validación
        print(f"Validando transferencia con código {self.codigo_confirmacion}...")
        self.validada = True

    def procesar_pago(self,monto):
        if not self.validada:
            raise Exception("La transferencia no ha sido validada.")
        print(f"Procesando pago de {monto} en efectivo. Mediante Transferencia Bancaria.")


# Pagos en efectivo
class PagoEnEfectivo(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Procesando el pago de {monto} en efectivo. No se necesita validación.")


def realizar_pago(metodo_pago, monto):
    if isinstance(metodo_pago, Metodovalidable):
        metodo_pago.validar()
    metodo_pago.procesar_pago(monto)

# Uso con diferentes métodos
tarjeta = TarjetaDeCredito("1234-5678-9012-3456", "123")
transferencia = TransferenciaBancaria("CONFIRM123")
efectivo = PagoEnEfectivo()

realizar_pago(tarjeta, 100)        
realizar_pago(transferencia, 200)
realizar_pago(efectivo, 50)

"""EJERCICIO TERMINADO!, aprendí la funcíon incorporada "isinstance", libreria abc para un módulo estándar llamado Abstract Base Classes (Clases Base Abstractas). 
Se utiliza para definir clases abstractas y asi garantizar que las subclases implementen ciertos métodos obligatorios.
"""