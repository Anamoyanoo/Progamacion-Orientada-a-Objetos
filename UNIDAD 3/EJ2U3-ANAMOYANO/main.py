import csv
import precios as p
from helado import Helado
from sabor import Sabor
from manejadorHelado import ManejadorHelado
from manejadorSabores import ManejadorSabores

if __name__ == '__main__':
	sabores=ManejadorSabores()
	sabores.carga()
	helados=ManejadorHelado()
	print("1. Vender helado \n2. Mostrar los 5 sabores mas vendidos")
	print("3. Ver total de gramos vendidos por sabor")
	print("4. Mostrar todos los sabores vendidos en un tipo de helado")
	print("5. Determinar importe recaudado por cada tipo de helado")
	opc=input('Ingrese la opcion: ')
	while opc!=0:
		if opc=='1':
			helados.venderHelado(sabores)
		elif opc=='2':
			helados.saboresMasVendidos(sabores)
		elif opc=='3':
			sabor=int(input("Ingrese id de sabor: "))
			helados.gramosXsabor(sabor,sabores)
		elif opc=='4':
			for k,v in p.tHelado.items():
				print(f"{k}) {v[0]:5}gr ${v[1]:5>}")
			tipo=input("Ingrese un tipo de heladinio: ")
			gramos=p.tHelado[tipo][0]
			helados.saboresXtipoHelado(gramos,sabores)
	print("1. Vender helado /n 2. Mostrar los 5 sabores mas vendidos")
	print("3. Ver total de gramos vendidos por sabor")
	print("4. Mostrar todos los sabores vendidos en un tipo de helado")
	print("5. Determinar importe recaudado por cada tipo de helado")
	opc=input('Ingrese la opcion: ')