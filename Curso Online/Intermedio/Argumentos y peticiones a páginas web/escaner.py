import argparse
import requests 
coolurl = ""
parser = argparse.ArgumentParser(description="Escaner de version de servidor")
parser.add_argument('-u','--url',dest="coolurl",help="Especifica la URL a escanear", required=True)
##Trabajando con argumentos de un comando
arguments = parser.parse_args()

if arguments.coolurl: #ver si tiene contenido los argumentos.. :)
	request = requests.get(url=arguments.coolurl, verify=False) #verify para que no de fallos con el ssl
	headers = dict(request.headers)
	#print(headers)
	if headers['Server']:
		print ("El servidor es: {}".format(headers["Server"]))
	else:
		print("No se pudo detectar la version")
