class PlanAhorro:
    __codplan = 0
    __mod = ''
    __version = ''
    __valor = int('0')
    __cancuotas = int('60')
    __cancuotaspagas = int('10')
    
    def __init__(self,codplan=0,mod='',ver='',valor='',cancuotas='',canpagas=''):
        self.__codplan = int(codplan)
        self.__mod= mod
        self.__ver= ver
        self.__valor = int(valor)
    def __str__(self):
        return '{}  {}  {} {}'.format(self.__codplan,self.__mod,self.__ver,self.__valor)
    def mostrarcod(self):
        return self.__codplan
    def mostrarmodelo(self):
        return self.__mod
    def mostrarversion(self):
        return self.__ver
    def mostrarvalor(self):
        return self.__valor
    def mostrarcuotas(cls):
        return cls.cancuotas
    def mostrarcuotaspagas(cls):
        return cls.cancuotaspagas
    def actualizarplan(self,valornuevo):
        self.__valor = valornuevo
        return
    def calcularcuota(self):
        cuota=int((self.__valor/self.__cancuotas) + self.__valor * 0.10)
        return cuota
    def verif(self,codigo):
        if int(self.__codplan) == int(codigo):
            return True
    def valorlic(self):
        cuota=int((self.__valor/self.__cancuotas) + self.__valor * 0.10)
        licit = int(self.__cancuotaspagas * cuota)
        return licit
    def modificarcuotalicitacion(self,nuevalicitacion):
        self.__cancuotaspagas=nuevalicitacion
        return