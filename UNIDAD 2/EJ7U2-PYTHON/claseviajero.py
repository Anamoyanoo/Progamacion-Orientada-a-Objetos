class ViajeroFrecuente():
    __numviajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasacum = 0

    def __init__(self, numv = "", doc = "", nom = "", ape = "", macum=0):
        self.__numviajero = numv
        self.__dni = doc
        self.__nombre = nom
        self.__apellido = ape
        self.__millasacum = macum
    def __gt__(self,otro):
        return self.__millasacum > otro.cantTotalMillas()
    def mostrarnom(self):
        print('El viajero con mayor cantidad de millas acumuladas es: {}'.format(self.__nombre))
    def __radd__(self,otro):
        self.__millasacum += otro
        return otro
    def __rsub__(self,otro):
        self.__millasacum -=otro
    def mostrarmillas(self):
        return self.__millasacum
    def cantTotalMillas(self): 
        return self.__millasacum 
    def canjearMillas(self, cantcan):
        if cantcan <= self.__millasacum:
            self.__millasacum = self.__millasacum - cantcan
            print('Millas canjeadas')
        else: print("No se pudo realizar el canje")
        return
    def mostrar(self):
        print('El viajero numero {} es {} {} con DNI {} y un total de millas acumuladas de {}'.format(self.__numviajero,self.__nombre,self.__apellido,self.__dni,self.__millasacum))           
    def verifnum(self, numero):
        if self.__numviajero == numero:
            return True
    def ingreso(lista):
        numviajero = input("Ingrese un numero de viajero: ")
        for i in range(len(lista)):
            if lista[i].verifnum(numviajero) == True:
                return i