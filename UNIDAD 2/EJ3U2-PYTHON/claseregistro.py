class Registro:
    __temperatura= 0
    __humedad= 0
    __presionatmosferica= 0 
    def __init__(self,temp,hum,pres):
        self.__temperatura = float(temp)
        self.__humedad = float(hum)
        self.__presionatmosferica = float(pres)
    def __str__(self):
        return '{}     {}     {}'.format(self.__temperatura,self.__humedad,self.__presionatmosferica)
    def mostrartemp(self):
        return self.__temperatura
    def mostrarhum(self):
        return self.__humedad
    def mostrarpres(self):
        return self.__presionatmosferica