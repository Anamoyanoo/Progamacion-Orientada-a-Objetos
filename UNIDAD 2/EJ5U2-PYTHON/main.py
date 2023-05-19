from claseplanahorro import PlanAhorro
from manejador import Controlador
import csv
if __name__ == '__main__':
    lista = Controlador()
    lista.leerarchivo() 
    print('1.Cambiar valor')
    print('2.Mostrar vehiculos con cuota inferior a la indicada')
    print('3.Mostrar la cantidad paga para licitar')
    print('4.Cambiar cantidad de cuotas pagas')
    print('5.Salir')
    opc = int(input("Ingrese opcion: "))
    while opc !=5:
        if opc == 1:
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
            lista.actualizar()
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
        elif opc == 2:
            cuota=int(input("Ingrese un valor de cuota: "))
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
            lista.planinferior(cuota)
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
        elif opc == 3:
            codigo = int(input("Ingrese codigo de auto para ver la cantidad de cuotas pagas para poder licitar: "))
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
            print(lista.licitacion(codigo))
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-,-.-.-.-.-.-.-.-.-.-.-.-.-')
        elif opc == 4:
            lista.modificarlicitacion()
        print('1.Cambiar valor')
        print('2.Mostrar vehiculos con cuota inferior a la indicada')
        print('3.Mostrar la cantidad paga para licitar')
        print('4.Cambiar cantidad de cuotas pagas')
        print('5.Salir')
        opc = int(input("Ingrese opcion: "))