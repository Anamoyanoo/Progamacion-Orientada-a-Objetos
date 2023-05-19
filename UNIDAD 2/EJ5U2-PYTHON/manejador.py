from claseplanahorro import PlanAhorro
import csv
class Controlador:
    def __init__(self):
        self.__lista=[]
        return
    def leerarchivo(self):
        archivo = open('planes.csv')
        leer = csv.reader(archivo,delimiter=';')
        for fila in leer:
            self.__lista.append(PlanAhorro(fila[0],fila[1],fila[2],fila[3]))     
    def muestra(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
        return
    def actualizar(self):
        for plan in self.__lista:
            print(plan)
            valornuevo = int(input("Ingrese nuevo valor del plan, ingrese 0 para no actualizar: "))
            if valornuevo>0:
                plan.actualizarplan(valornuevo)
        return
    def planinferior(self,cuota):
        for valor in self.__lista:
            if valor.calcularcuota()<cuota:
                print(valor)
        return
    def licitacion(self,codigo):   
        for cod in self.__lista:
            if cod.verif(codigo) == True:
                return "Para licitar el vehiculo la cantidad paga debe ser de: {}".format(cod.valorlic())
    def modificarlicitacion(self):
        cod=int(input("Ingrese codigo de plan: "))
        i=-1
        bandera=False
        while not bandera and i<len(self.__lista):
            i+=1
            bandera=self.__lista[i].mostrarcod()==cod
        if not bandera:
            print("No se encontro el plan con ese codigo")
        else:
            nueva=int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
            self.__lista[i].modificarcuotalicitacion(nueva)
        return