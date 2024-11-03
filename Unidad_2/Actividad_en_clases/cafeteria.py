from typing import Any


class Cafeteria():
    descuento = 0.1
    def __init__(self,nombre,menu,pedidos,producto,valor):
        self.__nombre = nombre
        self.__menu = []
        self.__pedidos = []

    