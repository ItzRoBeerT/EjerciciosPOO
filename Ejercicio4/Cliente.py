class Cliente:
    __nombre:str
    __cantidad:float

    def __init__(self, nombre,cantidad):
        self.__nombre = nombre
        self.__cantidad = cantidad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor

    def depositar(self, cantidad):
        self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


    def __str__(self):
        return f"Nombre: {self.__nombre} Cantidad de dinero: {self.cantidad}"