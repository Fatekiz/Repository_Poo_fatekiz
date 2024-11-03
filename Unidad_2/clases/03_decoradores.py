class Doctor():
    def __init__(self,nombre,especialidad,salario):
        #Atributos privados
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__salario = salario

    # Con el decorador para asi poder acceder a él como si fuera un atributo
    @property
    def nombre(self):      
        return self.__nombre    
    
    @nombre.setter
    def nombre(self,new_name):        
        if len(new_name)> 0:
            self.__nombre = new_name
        else:
            print("Error: El nombre no puede estar vacio.")
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self,new_salario):
        if new_salario < 0:
            print("Error: El salario no puede ser negativo")
        else:
            self.__salario = new_salario 
    @property
    def especialidad(self):
        return self.__especialidad
    @especialidad.setter
    def especialidad(self,new_especialidad):
        if len(new_especialidad) < 0:
            print("Error: La especialidad nueva debe tener un nombre.")
        else:
            self.__especialidad = new_especialidad
        

    
    def mostrar_info(self):
        print(f"Informacion del doctor: \n nombre: {self.__nombre} | especialidad: {self.__especialidad} | salario: ${self.__salario} ")


# Creación
doctor1 = Doctor("Dr. Benjamin Concha","cirujano",5000)
doctor1.mostrar_info()
print(doctor1.nombre)
doctor1.nombre = "Dra Rocío Cárdenas"
doctor1.mostrar_info()
doctor1.salario = 5500
print(f"El nuevo salario de la Dra es: ${doctor1.salario}")
doctor1.especialidad = "Cirujano plástico"
print(doctor1.especialidad)

doctor1.mostrar_info()