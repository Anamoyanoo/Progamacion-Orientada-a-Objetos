class TallerCapacitacion(object):
	def __init__(self,idTaller,nombre,vacantes,monto):
		self.__idTaller = idTaller
		self.__nombre = nombre
		self.__vacantes = vacantes
		self.__monto = monto
	def mostrarDatosTaller(self):
		print(f"id: {self.__idTaller}\n{self.__nombre}\nVac. disponibles{self.__vacantes}\nPrecio: {self.__monto}\n")
	def idTaller(self):
		return self.__idTaller  