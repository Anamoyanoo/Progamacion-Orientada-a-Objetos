from claseregistro import Registro
from controlador import Manejador

if __name__ == '__main__':
    liista=Manejador()
    Manejador.leerarc(liista)
    print("Opcion 1: Mostrar el dia y hora de menor y mayor valor de la temperatura, la humedad y la presion atmosferica")
    print("Opcion 2: Indicar la temperatura promedio mensual por cada hora")
    print("Opcion 3: Mostrar los parametros meteorologicos de un dia")
    print("Opcion 4: Salir")
    opc = int(input("Ingrese opcion: "))
    while opc!=4:
        if opc == 1:
            Manejador.accion1(liista)
        elif opc ==2:
            Manejador.accion2(liista)
        elif opc == 3:
            Manejador.accion3(liista)
        print("Opcion 1: Mostrar la el dia y hora de menor y mayor valor")
        print("Opcion 2: Indicar la temperatura promedio mensual por cada hora")
        print("Opcion 3: Mostrar los parametros meteorologicos de un dia")
        print("Opcion 4: Salir")
        opc = int(input("Ingrese nuevamente una opcion: "))
        