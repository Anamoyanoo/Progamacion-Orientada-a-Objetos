from sabor import Sabor
import csv
class ManejadorSabores:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def carga(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            crear=Sabor(fila[0],fila[1],fila[2])
            self.__lista.append(crear)
        archivo.close()
    def mostrarSabores(self):
        for sabor in self.__lista:
            print(sabor)
    def sabor(self,i):
        return self.__lista[i-1]
    def test(self):
        self.cargar()
        self.mostrarSabores()
    def verifSabor(self,indice):
        if self.sabor(indice) not in self.__lista:
            indice=int(input("Codigo erroneo, ingrese sabor"))
            indice=self.verifSabor()
        return indice
    def len(self):
        return len(self.__lista)
    
if __name__ == '__main__':
	man=ManejadorSabores()
	man.test()