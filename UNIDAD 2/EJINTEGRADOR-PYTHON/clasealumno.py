class alumnos:
    __dni=''
    __apellido=''
    __nombre=''
    __carrera=''
    aniocursado=''
    def __init__(self,dni,apellido,nombre,carrera,aniocursado):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.aniocursado=aniocursado
    def __str__(self):
        return "{} {} {} {} {}".format(self.__dni,self.__apellido,self.__nombre,self.__carrera,self.aniocursado)
    def getdni(self):
        return self.__dni
    def getapellido(self):
        return self.__apellido
    def getnombre(self):
        return self.__nombre
    def getcarrera(self):
        return self.__carrera
    def getanio(self): #modificaraño
        return self.aniocursado
    def verificardni(self,dni):
        return self.__dni == dni