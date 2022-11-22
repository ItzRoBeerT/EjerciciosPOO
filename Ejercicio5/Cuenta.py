class Cuenta:
    __titular:str
    __cantidad:float

    def __init__(self, titular, cantidad):

        self.__titular = titular
        self.__cantidad = cantidad

    def __str__(self):
        return f"Titular: {self.__titular} Cantidad:{self.__cantidad}\n"
