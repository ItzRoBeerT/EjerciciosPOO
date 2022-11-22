class Persona:
    __nombre:str
    __edad: int

    def  __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre= valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,valor):
        self.__edad = valor

    def isMayorEdad(self):
        if self.__edad > 18:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad}"
