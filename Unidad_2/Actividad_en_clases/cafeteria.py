class Cafeteria():
    descuento = 0.1
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__menu = {} # Diccionario para los menús
        self.__pedidos = []

    def agregar_menu(self,name,valor):
        assert valor > 0 , "Error: El valor no puede ser negativo"
        if not self.__producto_existente(name):
            self.__menu[name] = valor
            print(f"El producto '{name}' ha sido agregado al menú con el precio: ${valor}.")
        else:
            print(f"El producto '{name}' ya se encuentra en el menu")

    # accesor privado   
    def __producto_existente(self, nombre_producto):
        return nombre_producto in self.__menu

    def agregar_pedido(self,producto):
        assert self.__producto_existente(producto), f"Error: El producto no se encuentra en el menu"
        self.__pedidos.append({producto: self.__menu[producto]})

    def mostrar_menu(self):
        print("Menú de la Cafetería:")
        for producto,precio in self.__menu.items():
            print(f"{producto}: ${precio}")

    def mostrar_pedidos(self):
        print("Pedidos: ")
        for pedido in self.__pedidos:
            for producto,precio in pedido.items():
                print(f"Nombre del plato: {producto}, Precio: ${precio}")

    #método para calcular el toral del pedido y desc. para cliente frecuente.
    def calcular_total(self,frecuente):
        total = 0
        for pedidos in self.__pedidos:
                for nombre, precio in pedidos.items():
                    total += precio
        if frecuente:
            total -= total * Cafeteria.descuento
            print(f"\n (frecuente) Eres cliente frecuente! recibiste un descuento del 10%")
            print(f"Total a pagar: ${int(total)}")
        else:
            print(f" \n  (no frecuente) Tu total a pagar es de: ${total}")

    # métdo estático | para que los usuarios simulen una compra con descuento
    @staticmethod
    def simular_descuento(monto,descuento):
        assert monto > 0 and descuento >0 , "Error: el monto y el descuento deben ser mayores a 0"
        descuento_f = monto * descuento
        total = monto - descuento_f
        print(f"\n--Simulación completada--\n monto de prueba: {monto}\n descuento de prueba: {descuento} \n - Total a pagar : ${total} -  (se aplicó un descuento de: ${descuento_f})")



cafe = Cafeteria("Rocys")
cafe.agregar_menu("cancato",10000)
cafe.agregar_menu("sopaipillas",300)
cafe.agregar_menu("pan_aliado",3000)
cafe.agregar_menu("cancato",1)
cafe.agregar_pedido("pan_aliado")
cafe.agregar_pedido("cancato")
cafe.agregar_pedido("sopaipillas")
cafe.mostrar_menu()
cafe.mostrar_pedidos()
cafe.calcular_total(True)
cafe.calcular_total(False)
cafe.simular_descuento(1000,0.1)