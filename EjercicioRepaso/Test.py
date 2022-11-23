from random import randint
def generarMenu():
    print('''
           Color                    DESCUENTO
        
        Bola Blanca                No tiene
        Bola Roja                  10 por ciento
        Bola Azul                  20 por ciento
        Bola Verde                 25 por ciento
        Bola Amarilla              50 por ciento
    ''')

dinero = input("Introduzca cantidad a pagar ")

if float(dinero) <100:
    print("No se aplica promoción")
else:
    numAl = randint(0,5)

generarMenu()




