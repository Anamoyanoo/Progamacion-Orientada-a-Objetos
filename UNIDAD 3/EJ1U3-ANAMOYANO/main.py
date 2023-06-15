import csv
from Clasecarrera import Carrera
from Clasefacultad import Facultad
from Manejafacultad import manejadorfacultad

if __name__ == '__main__':
	facultades=manejadorfacultad()
	facultades.cargar()
	print("""
1) Mostrar carreras de una facultad
2) Mostrar codigo carrera
		""")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				codigo=int(input("Ingrese codigo facultad: "))
				facultades.mostrarCarrerasFacultad(codigo)
			case 2:
				carrera=input("Ingrese nombre carrera: ")
				facultades.buscarCarrera(carrera)
		print("""
1) Mostrar carreras de una facultad
2) Mostrar codigo carrera
		""")
		opc=int(input(""))