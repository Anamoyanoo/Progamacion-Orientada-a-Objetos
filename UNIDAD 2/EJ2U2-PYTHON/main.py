import csv
from ejercicio2 import ViajeroFrecuente
if __name__ == "__main__":
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo,delimiter=',')
    listaviajeros = []
    for fila in reader:
        listaviajeros.append(ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4]))
    for i in range(len(listaviajeros)):
        listaviajeros[i].mostrar()
    numviaj = ViajeroFrecuente.ingreso(listaviajeros)
    print ("1. Consultar millas ")
    print ("2. Acumular ")
    print ("3. Canjear ")
    print ("4. Salir ")
    opc = int(input("Ingrese opcion: ")) 
    while opc !=4:
        if opc == 1:
            print("La cantidad de millas es: {}".format(listaviajeros[numviaj].cantTotalMillas()))
        elif opc == 2:
            millas= int(input("Ingrese cantidad de millas a acumular: ")) 
            listaviajeros[numviaj].acumularMillas(millas)
        elif opc == 3:
            millasACanjear = int(input("Ingrese la cantidad de millas a canjear: "))
            listaviajeros[numviaj].canjearMillas(millasACanjear)
        opc = int(input("Ingrese opcion: "))