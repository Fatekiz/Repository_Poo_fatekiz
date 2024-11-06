class Doctor():
    def __init__(self,nombre,especialidad,salario):
        #Atributos privados
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__salario = salario

    # Getter para el nombre / get_x
    def get_nombre(self):      # usamos el prefijo get para "obtener" un atributo.
       return self.__nombre    # nos retorna el atributo privado, en este caso el nombre
    
    # Setter para el nombre / set_x
    def set_nombre(self,new_name):        # método para cambiar un atributo privado
        if len(new_name)> 0:
            self.__nombre = new_name
        else:
            print("Error: El nombre no puede estar vacio.") 

    def mostrar_info(self):
        print(f"Informacion del doctor: \n nombre: {self.__nombre} | especialidad: {self.__especialidad} | salario: ${self.__salario} ")


# Creación
doctor1 = Doctor("Dr. Benjamin Concha","cirujano",5000)
doctor1.mostrar_info()
print(doctor1.__nombre)
doctor1.set_nombre("Dra Rocio Cárdenas") # gracias al método cambie un atributo privado.
doctor1.mostrar_info()