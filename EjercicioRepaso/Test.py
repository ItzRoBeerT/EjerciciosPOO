from random import randint
def generarMenu():
    print('''
        * * * * * * * * * * * * * * * * * * * * *
       *    Color                    DESCUENTO    *
       *                                          *
       * Bola Blanca                No tiene      * 
       * Bola Roja                  10 por ciento *
       * Bola Azul                  20 por ciento * 
       * Bola Verde                 25 por ciento *
       * Bola Amarilla              50 por ciento *
        * * * * * * * * * * * * * * * * * * * * * 
    ''')

dinero = input("Introduzca cantidad a pagar ")
descuento= 0
if float(dinero) <100:
    print("No se aplica promoción")
else:
    generarMenu()
    numAl = randint(0,5)
    if numAl ==0:
        print("Te ha tocado la blanca")
    elif numAl == 1:
        print("Te ha tocado la roja")
        descuento= 10
    elif numAl ==2:
        print("Te ha tocado la azul")
        descuento = 20
    elif numAl ==3:
        print("Te ha tocado la verde")
        descuento = 25
    elif numAl ==4:
        print("Te h tocado la amarilla")
        descuento = 50

if  descuento == 0:
    print(f"No ha conseguido ningun descuento\nPrecio: {dinero}$")
else:
    dineroDesc = (float(dinero)*descuento)/100
    dinero = float(dinero)-dineroDesc
    print(f"Ha coneguido un descuento de {descuento}%\nNuevo precio: {dinero}$")









