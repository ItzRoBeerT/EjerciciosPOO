class Calculadora:
    __numero1:float
    __numero2:float

    def __init__(self, numero1, numero2):
        self.__numero1= numero1
        self.__numero2 = numero2

    @property
    def numero1(self):
        return self.__numero1
    @numero1.setter
    def numero1(self, valor):
        self.__numero1 = valor

    @property
    def numero2(self):
        return self.__numero2
    @numero2.setter
    def numero2(self, valor):
        self.__numero2 = valor

    def sumar(self):
        return self.__numero1+self.__numero2

    def restar(self):
        return self.__numero1-self.__numero2

    def multiplicar(self):
        return self.__numero1*self.__numero2

    def dividir(self):
        return self.__numero1/self.__numero2
    


