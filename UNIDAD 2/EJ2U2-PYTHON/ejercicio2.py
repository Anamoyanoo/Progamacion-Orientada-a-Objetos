class ViajeroFrecuente:
    __numviajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasacum = 0

    def __init__(self, numv = "", doc = "", nom = "", ape = "", macum = 0):
        self.__numviajero = numv
        self.__dni = doc
        self.__nombre = nom
        self.__apellido = ape
        self.__millasacum = int(macum)
    def cantTotalMillas(self): 
        return self.__millasacum 
    def acumularMillas(self, cant=0):
        self.__millasacum = self.__millasacum + cant
        print('La cantidad es {}'.format(self.__millasacum))
        return
    def canjearMillas(self, cantcan):
        if cantcan <= self.__millasacum:
            self.__millasacum = self.__millasacum - cantcan
            print('Millas canjeadas')
        else: print("No se pudo realizar el canje")
        return
    def mostrar(self):
        print('El numero de viajero es: {}'.format(self.__numviajero))
        print('El DNI es: {}'.format(self.__dni))
        print('El nombre es: {}'.format(self.__nombre))
        print('El apellido es: {}'.format(self.__apellido))            
        print('Las millas acumuladas son: {}'.format(self.__millasacum))
    def verifnum(self, numero):
        if self.__numviajero == numero:
            return True
    def ingreso(lista):
        numviajero = input("Ingrese un numero de viajero: ")
        for i in range(len(lista)):
            if lista[i].verifnum(numviajero) == True:
                return i