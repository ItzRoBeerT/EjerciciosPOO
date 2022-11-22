class Banco:
    __clientes:list

    def __init__(self, clientes):
        self.__clientes = clientes

    def depositoTotal(self):
        deposit_total: float=0
        for cliente in self.__clientes:
            deposit_total= deposit_total+ cliente.cantidad
        return deposit_total

    def operar(self):
        #TODO
        return 0

    def __str__(self):
        return f"Depósito total: {self.depositoTotal()}"


