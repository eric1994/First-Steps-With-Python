#-*- coding:UTF-8 -*-
import psycopg2

conexion_string ="dbname='clase_db' host='localhost' user='eric' password='imagic'"

try: 
	conexion = psycopg2.connect(conexion_string)
except:
	print ("No se pudo conectar!")
	exit(0)

cur = conexion.cursor()
query = "select * from pruebas"
cur.execute(query)
resultado = cur.fetchall()

for dato in resultado:
	print(str(dato[0]) + "\t" + dato[1] + "\t" + dato[2]) 