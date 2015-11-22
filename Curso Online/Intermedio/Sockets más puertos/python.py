##Escaner de puertos
import socket

def escanear_puerto(ObjHost, ObjPuerto):
	try:
		conexion = socket.socket()
		conexion.settimeout(1)
		conexion.connect((ObjHost,ObjPuerto))
		conexion.send(b'Exploiter.co')
		print("{}/tcp Abierto".format(ObjPuerto))
	except:
		print("{}/tcp Cerrado".format(ObjPuerto))

	finally:
		conexion.close()

puertos = [21, 22, 80, 445, 139, 8080]
for puerto in puertos:
	escanear_puerto('192.168.1.131',puerto)
