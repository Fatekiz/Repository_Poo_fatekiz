# clase de encapsulamiento
#                             <-- diagrama de clase, nada que ver con programacion


# |ENCAPSULACIÓN|

# ° Al vrear una clase estamos resguardando algo (atributos y metodos) 
# °° Es un mecanismo que permite que los datos puedan trabajar agrupados en una sola unidad sintática °°
# °°°  Pero tambioén es un metodo abstracción, (protección de datos) que hace que no todos puedan acceder a los datos del interior (visibilidad, privado) °°


# En mecanismo de protección 
# estos pueden ser visibles hasta cierpo punto y los marcaremos como visibles o publicos segun queramos

# °° con doble guíon bajo |solo al principio| marcariamos en privado un dato

#ejemplo

class Test:
    def __uno(sef):
        print("Este método es privado, ya que su nombre empieza por __")
    def dos(sef):
        print("Este método es publico")
    def __tres__(sef):
        print("Este metodo también es público, ya que empieza y termina con __ ")
test1 = Test()
test1.__uno()
test1.dos()
test1.__tres__()