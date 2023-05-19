class Conjunto():
	__conjunto=[]
	def __init__(self,lista):
		self.__conjunto=lista
	def __add__(self,otro):
		if isinstance(otro,Conjunto):
			for i in otro.__conjunto:
				if not i in self.__conjunto:
					self.__conjunto.append(i)
		# esta solucion no era apta cuando habian elementos repetidos
		# 	self.__conjunto.extend(otro.__conjunto)
		if isinstance(otro,int):
			self.__conjunto.append(otro)
		return self
	def __radd__(self,otro):
		if isinstance(otro,int):
			self.__conjunto.append(otro)
		return self
	def __str__(self):
		return f"{self.__conjunto}"
	def __sub__(self,otro):
		if isinstance(otro,Conjunto):
			for i in otro.__conjunto:
				if i in self.__conjunto:
					self.__conjunto.pop(self.__conjunto.index(i))
		elif isinstance(otro,int):
			if otro in self.__conjunto:
				self.__conjunto.pop(self.__conjunto.index(otro))
		return self
	def __rsub__(self,otro):
		if isinstance(otro,int):
			if otro in self.__conjunto:
				self.__conjunto.pop(self.__conjunto.index(otro))
		return self
	def __eq__(self,otro):
		if isinstance(otro,Conjunto):
			if len(otro.__conjunto)==len(self.__conjunto):
				i=0
				bandera=True
				while bandera and i<len(self.__conjunto):
					if not(otro.__conjunto[i] in self.__conjunto):
						bandera=False
					i+=1
			else:
				bandera=False
		else:
			bandera=False
		return bandera