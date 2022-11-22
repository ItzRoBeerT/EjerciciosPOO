from Ejercicio5.Cuenta import Cuenta


class CajaAhorro(Cuenta):

    def __init__(self,titular,cantidad):
        Cuenta.__init__(self,titular,cantidad)

    def __str__(self):
        return f"{Cuenta.__str__(self)}"