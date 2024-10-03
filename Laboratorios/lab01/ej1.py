# 1. Clase Personaje:
""" ○ Atributos: el nombre del personaje, 
el nivel de vida del personaje y los           <-- listo
puntos de ataque del personaje.         """  

"""
○ Métodos:

 un método que permita que el personaje ataque a otro,
disminuyendo la vida del otro personaje según los puntos de ataque del      <-- listo
atacante. 

Un segundo método, que verifique si el personaje sigue vivo. Debe       <-- listo
devolver True si el nivel de vida es mayor a 0, y False si no.  


Por último: implementar un método mágico 
que permita devolver un string que muestre                <-- listo
el estado del personaje (nombre, vida, y ataque). 




"""


class Personaje():
    def __init__(self,nombre,vida,ataque): #contructor de clase
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self,objetivo,n_ataque): # n_ataque = cuantos ataques desea hacer 
        vida_menos = self.ataque * n_ataque # ej 25(atac) * 3(golpes) = 75 
        objetivo.vida -= vida_menos # actualizo variable del objetivo
        print(f"El personaje '{self.nombre}' ha atacado a '{objetivo.nombre}' con {n_ataque} golpes y le ha quitado: {vida_menos} puntos de vida")
        print(f"La vida de {objetivo.nombre} ha disminuido a {objetivo.vida} ")        

    def verificar_vida(self):
        if self.vida >= 0:
             print(self.vida> 0)
        else:
            print(self.vida > 0)

    def __str__(self): # para verificar el estado del personaje
        return f" \n Estado de Personaje: \n \n  {self.nombre}\n pts. de vida: {self.vida}\n pts. de ataque: {self.ataque}"


            
# instanciar: 
personaje1 = Personaje("jose", 95, 25)
personaje2 = Personaje("vicente", 100, 30)

personaje1.atacar(personaje2,3) # dejar a vicente con 25 de vida
personaje2.atacar(personaje1,3)
personaje2.verificar_vida() # viendo la vida de vicente
personaje1.verificar_vida()
personaje1.atacar(personaje2,1) # matar a vicente
personaje2.verificar_vida()

#verificando estados de personajes
print(personaje1)
print(personaje2)