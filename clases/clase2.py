#                                                              ------- CLASE DE "CLASES MÁGICAS" -------

class Triangulo():
    
    #Constructor de clase
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    # Método mágico que devuelve una representación en cadena del triángulo
    def __str__(self):
        return f"El triángulo tiene los siguientes lados: {self.l1} cm, {self.l2} cm, {self.l3} cm."
    
    # Método mágico que comprueba si dos triángulos son iguales o no
    def __eq__(self, triangle):
        return {self.l1, self.l2, self.l3} == {triangle.l1, triangle.l2, triangle.l3}
    
    # Método mágico que permite sumar 2 triángulos
    def __add__(self, triangle):
        return Triangulo(
            self.l1 + triangle.l1,
            self.l2 + triangle.l2,
            self.l3 + triangle.l3,
        )
    
    # Método mágico que devuelve el perímetro del triángulo
    def __len__(self,):
        return int(self.l1 + self.l2 + self.l3)
    
    # Verifica si los lados ingresados forman un triángulo valido
    def es_valido(self):
        return (self.l1 + self.l2 > self.l3 and self.l1 + self.l3 > self.l2 and self.l2 + self.l3 > self.l1)
    

# Creando 2 instancias (Obhjeto) de la clase triángulo
triangulo1 = Triangulo(3,4,5)
triangulo2 = Triangulo(11,12,13)

# se llama el método __str__ para representar el triángulo como una cadena
print(triangulo1)

# se llama el metodo __eq__ para ver si los triángulos son iguales
print(triangulo1 == triangulo2)

# se ocupa el metodo __add__ para sumar los triángulos
triangulo3= triangulo1 + triangulo2
print(triangulo3)

# se ocupa el metodo __len__ para obtener el perimetro del triangulo
print(len(triangulo1))

# se ocupa el metodo es_vaido() para verificar si los triangulos son váidos
print(triangulo1.es_valido())
print(triangulo2.es_valido())

# Clase terminada, entendí casi todo