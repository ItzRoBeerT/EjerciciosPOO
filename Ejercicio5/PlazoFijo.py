from Ejercicio5.Cuenta import Cuenta


class PlazoFijo(Cuenta):

    def __init__(self,titular,cantidad,plazo, interes):
        Cuenta.__init__(self, titular, cantidad)
        self.__plazo = plazo
        self.__interes = interes
    def calcImporteInteres(self):
        resul:float = (self.__plazo*self.__interes/100)
        return resul

    def __str__(self):
        return f"{Cuenta.__str__(self)}Plazo: {self.__plazo} " \
               f" Intereses: {self.__interes} Total de interés: {self.calcImporteInteres()}"
    

