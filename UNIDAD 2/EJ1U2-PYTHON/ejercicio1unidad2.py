import csv
class Email():
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contraseña = ""
    def __init__(self, Cuenta = "", domini = "", tipoDomi = "", contra = ""):
        self.__idCuenta = Cuenta
        self.__dominio = domini 
        self.__tipoDominio = tipoDomi
        self.__contraseña = contra

    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"

    def getDominio(self):
        return self.__dominio

    def CrearCuenta(self, direccionDeCorreo):
        partes = direccionDeCorreo.split('@')
        self.__idCuenta = partes[0]
        __DominioyTipo = partes[1].split('.')
        self.__dominio = __DominioyTipo[0]
        self.__tipoDominio = __DominioyTipo[1]

if __name__ == "__main__":
    email = Email()
    nombre = input("Ingrese su nombre ")
    mail = input("Ingrese el email ")
    contraseña = input("Ingrese la contraseña ")
    email.CrearCuenta(mail)
    print("Estimado",nombre,"te enviaremos tus mensajes a la direccion: ", email.retornaEmail())
    comparar = input("Ingrese la contraseña actual ")
    if contraseña == comparar:
        nueva = input("Ingrese contraseña nueva ")
        contraseña= nueva
    else:
        print("La contraseña actual no coincide")
    correo = input("Ingrese el email ")
    email2= Email()
    email2.CrearCuenta(correo)
    archivo = open('ej1.csv')
    reader = csv.reader(archivo,delimiter=',')
    emails = []
    for fila in reader:
        if '@' in fila[0] and '.' in fila[0]:
            email3 = Email()
            email3.CrearCuenta(fila[0])
            emails.append(email3)
        else:
            print("La direccion {} es incorrecta".format(fila[0]))
    archivo.close()
    dominioingresado = input("Ingrese el dominio ")
    cont=0
    for email in emails:
        if dominioingresado == email.getDominio():
            cont+=1
    print("La cantidad de emails con ese dominio es: {}  ".format(cont))