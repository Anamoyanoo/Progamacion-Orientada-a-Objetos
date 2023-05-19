class Persona():
    __edad = 0
    __nombre = ""

    def __init__(self):
        self.__edad = [18, 20, 22, 21, 18, 20,22]
        self.__nombre = ["Ana","Maria", "belen","Guillermo"]
    def cargar(self, ed):
        self.__edad.append(ed)
    def mostrar(self):
        return self.__edad
    def mostrarnom(self):
        return self.__nombre
    def cargarnom(self, nom):
        self.__nombre.append(nom)
    def ordenar(self, minus):
        return self.__nombre.sort(key=minus)
    def consultar(self, elem):
        cant = self.__edad.count(elem)
        return cant
    def copiar(self):
        return self.__nombre.copy()


if __name__ == "__main__":
    pers = Persona()
    print("Las edades que ya se encuentran ingresadas son: ",pers.mostrar())
    print("Los nombres que ya se encuentran ingresados son: ", pers.mostrarnom())
    eda = int(input("Ingrese la edad a incorporar: "))
    nomb = input("Ingrese el nombre a incorporar: ")
    pers.cargar(eda)
    pers.cargarnom(nomb)
    print("Las edades ingresadas son: ",pers.mostrar())
    print("Los nombres ingresados son: ",pers.mostrarnom())
    minuscula = lambda cadena: cadena.lower()
    pers.ordenar(minuscula)
    print("Los nombres ordenados alfabeticamente son: ", pers.mostrarnom())
    elemento = int(input("Ingrese la edad a consultar: "))
    pers.consultar(elemento)
    print("La cantidad de personas con {} años es de: {}".format(elemento,pers.consultar(elemento)))
    pers2 = []
    pers2 = pers.copiar()
    print("Los nombres de la antigua lista son: ", pers.mostrarnom())
    print("Los nombres de la nueva lista son: {}".format(pers2))
    elimina = input("Ingrese el nombre a eliminar: ")
    pers2.remove(elimina)
    print("La lista nueva queda con los siguientes nombres: {}".format(pers2))
    pers2.clear()
    print("Los nombres que quedan en la lista nueva son: {}".format(pers2))