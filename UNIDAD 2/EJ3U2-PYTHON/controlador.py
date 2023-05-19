from claseregistro import Registro
import csv
class Manejador:    
    __lista=[]
    def __init__(self):
        self.__lista=[[]]
        return
    def leerarc(lista):
        archivo = open('datos.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            lista.cargar(fila)
    def cargar(self,registro):
        i=int(registro[0])
        if i>len(self.__lista):
            self.__lista.append([])
        self.__lista[i-1].append(Registro(registro[2],registro[3],registro[4]))    
    def mayortemp(self):
        i=0
        for dia in self.__lista:
            mayor = 0
            for hora in dia:
                if hora.mostrartemp()>mayor:
                    mayor = hora.mostrartemp()
            i+=1
            print("La mayor temperatura del día {} es: {}".format(i, mayor))
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    def mayorhum(self):
        i=0
        for dia in self.__lista:
            mayor = 0
            for hora in dia:
                if hora.mostrarhum()>mayor:
                    mayor=hora.mostrarhum()
            i+=1
            print("La mayor humedad del día {} es: {}".format(i, mayor))
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    def mayorpres(self):
        i=0
        for dia in self.__lista:
            mayor = 0
            for hora in dia:
                if hora.mostrarpres()>mayor:
                    mayor=hora.mostrarpres()
            i+=1
            print("La mayor presion del día {} es: {}".format(i, mayor))
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    def menortemp(self):
        i=0
        for dia in self.__lista:
            menor = 9999
            for hora in dia:
                if hora.mostrartemp()<menor:
                    menor=hora.mostrartemp()
            i+=1
            print("La menor temperatura del día {} es: {}".format(i, menor))
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    def menorhum(self):
        i=0
        for dia in self.__lista:
            menor = 9999
            for hora in dia:
                if hora.mostrarhum()<menor:
                    menor=hora.mostrarhum()
            i+=1
            print("La menor humedad del día {} es: {}".format(i, menor))
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    def menorpres(self):
        i=0
        for dia in self.__lista:
            menor = 9999
            for hora in dia:
                if hora.mostrarpres()<menor:
                    menor=hora.mostrarpres()
            i+=1
            print("La menor presion del día {} es: {}".format(i, menor))
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    def accion1(self):
        self.mayortemp()
        self.menortemp()
        self.mayorhum()
        self.menorhum()
        self.mayorpres()
        self.menorpres()
    def accion2(self):       
        i=0
        for hora in self.__lista:
            temp = 0
            con = 0
            for dia in hora:
                temp +=dia.mostrartemp()
                con +=1
            total = temp/con
            i+=1
            print("El promedio de la hora del mes {} es: {}".format(i, total))
        return
    def accion3(self):
        numdia = int(input("Ingrese el día para mostrar sus parámetros: "))
        espacio= ""*20
        print(f"Hora {espacio} Temperatura {espacio}  Humedad {espacio}   Presion")
        i=0
        for hora in self.__lista[numdia-1]:
            print(f" {i}  {espacio}    {hora.mostrartemp()}    {espacio}    {hora.mostrarhum()}    {espacio}    {hora.mostrarpres()}")
            i+=1
        return