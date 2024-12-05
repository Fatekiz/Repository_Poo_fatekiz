"""
Implementar una clase Fraccion que represente una fracción matemática con numerador y denominador. 
Además se debe crear varios métodos mágicos que permitan operar, comparar, y mostrar las fracciones de manera intuitiva. 
La clase debe poseer los siguientes métodos mágicos:

Método mágico que devuelva la fracción como una representación de cadena <-- listo

Método mágico que permita sumar dos fracciones <-- listo

Método mágico que permita el producto entre dos fracciones <-- listo

Método mágico que permita comparar dos fracciones. 
Dos fracciones se consideran iguales si sus valores numéricos son equivalentes.   

"""

class Fraccion():
    def __init__(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"\n'Fraccion': \n {self.numerador}\n - \n {self.denominador}"
    
    def __add__(self,fraccion):
        if self.denominador == fraccion.denominador:
            return Fraccion(
                self.numerador + fraccion.numerador,
                self.denominador
            )
        else:
            return "la Fraccion no se puede sumar, debido a que sus denominadores no son iguales"
        
    def __mul__(self,fraccion): # <-- método mágico para poder realiar multiplicaciones
        return Fraccion(
            self.numerador * fraccion.numerador,
            self.denominador * fraccion.denominador
        )
    
    def __truediv__(self,fraccion):
        fraccion1_1 = self.numerador / self.denominador
        fraccion2_2 = fraccion.numerador / fraccion.denominador
        if fraccion1_1 == fraccion2_2:
            return f"las fracciones son equivalentes."

        

        
    
    

    

fraccion1 = Fraccion(2,2)
fraccion2 = Fraccion(2,2)
fraccion3 = (fraccion1 + fraccion2) # para las sumas
fraccion4 = (fraccion1 * fraccion2) # para las multiplicaciones
fraccion5 = (fraccion1 / fraccion2) # para las divisiones y posterior comparación


print(fraccion1)
print(fraccion2)

print(fraccion3)
print(fraccion4)
print(fraccion5)