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
        nombreCli: str= input("Inserte nombre del cliente: ")
        for cli in self.__clientes:
            if nombreCli == cli.nombre:
                miCli = cli
                print("Bienvenido "+miCli.nombre+ "!")
                respuesta1 = input("Desea ingresar? (s/n)")
                if respuesta1.__eq__("s"):
                    cantidad:float = input("Inserte cantidad");
                    miCli.depositar(cantidad)
                respuesta2 = input("Desea retirar? (s/n)")
                if respuesta2.__eq__("s"):
                    cantidad: float = input("Inserte cantidad");
                    miCli.retirar(cantidad)
                print(miCli)
        return 0

    def __str__(self):
        return f"Depósito total: {self.depositoTotal()}"


