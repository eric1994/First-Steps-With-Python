import socket 



def banner(ObjHost,ObjPuerto):
	try:
		conexion = socket.socket()
		conexion.settimeout(1)
		conexion.connect((ObjHost,ObjPuerto))
		conexion.send(b'Exploiter.co')
		resultado = conexion.recv(1024)
		print("[+] {} Abierto".format(ObjPuerto))
		print(resultado)
	except:
		print("[-] {} Cerrado".format(ObjPuerto))
	finally:
		conexion.close()

puertos = [5050,500]
for puerto in puertos:
	banner('192.168.1.131',puerto)
