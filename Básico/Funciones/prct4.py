def di_hola():
	print("Hola Mundo")

def saludame(nombre):
	print ("Hola {}".format(nombre)) #simples funciones easy

di_hola()
saludame("Juan")

def agregar_dos(numero):
	if numero != 8:
		print(numero+2) 
	return numero+2 ##necesitamos un return

agregar_dos(5)
resultado = agregar_dos(8)
print (resultado)

