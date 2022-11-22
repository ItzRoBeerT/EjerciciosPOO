from Ejercicio4.Banco import Banco
from Ejercicio4.Cliente import Cliente

clientes:list=[]

cliente1 = Cliente("Roberto",1500)
clientes.append(cliente1)
cliente2 = Cliente("Manu",1200)
clientes.append(cliente2)
cliente3 = Cliente("Santiago",1000)
clientes.append(cliente3)

banco = Banco(clientes)

print(banco)


