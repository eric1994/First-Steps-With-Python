#!/usr/bin/python
# from blessings import Terminal  ###Probando modulos para colorinessss   // funciona pero dejo el de abajo para el end='' ** para este mirar documentacion en https://pypi.python.org/pypi/blessings/ y para instalar apt-get install python-blessings
from __future__ import print_function ##Jugando con el print, esto es para el end='' te obliga a poner los parentesis
import random
import time

# t = Terminal() ## Esto es del modulo de los colorines :)
 #######NOTA no puedo escribir enes ni tildes porque estoy ejecutando en consola y me viola el otro si lo hago. ALSO VIVA XUBUNTU
def Iniciar():
    print ('Estas en una tierra llena de golosinas, quieres comerte unas cuantas pero no sabes muy bien como',end=' ')  ##SI PONES UNA COMA QUITA EL SALTO DE LINEA
    print ('entonces.. se te ocurre una idea, por que no convertir un melocotonton salvaje que ves en el suelo',end=' ')
    print ('en una golosina y comertelo,... oye si en Dragon Ball convertian a uno en chocolate quien sabe',end=' ')
    print
    # print 'ESTO ' , 'SOLO ' , 'ES ' , 'UNA ' , 'PRUEBA DE PRINT'     Queria probar cosas guays de los prints pero no salio bien


def EligeOpcion():
     cave = ''
     opcion = ['1','2','3','4','5']
     bandera = True  ### Jugando con los booleanos

     while bandera:
         print('Quieres comer muchas golosinas dame un numero del 1 al 5 :)')    #Familiarizandonos con la estructura while.. distinto a uno y distinto a 2 
         cave += str(input())   # Conversion de tipo, del dato de entrada, el input equivaldria a un cin >> en c++ o un scanf("%d",dato) en C :D
         for i in opcion:  ## UN FOR NUNCA VIENE MAL ^^
            if cave == i:
              bandera = False
     return cave




def CompruebaOpcion(opcionelegida):
   print ('Parece que tienes ganas de comer golosinas....')
   time.sleep(2)                                                 #        Simples print y sleeps para hacer el texto mas interesante          
   print ('Aunque sea muy de noche...')
   time.sleep(2)
   print ('Matemos al melocotonton a ver que pasaaaa..')
   time.sleep(8)
   print('Te gusta esperar ehehehe.. no venga ya te lo digo')
   time.sleep(2)
   friendlyCave = str(random.randint(1, 5))   ##Le ponemos mas opciones para las risas
   # print (friendlyCave)
   if opcionelegida == friendlyCave: #otra conversion sersy
          print('No te lo crees ni tu meneno, mataste al melocotonton y estas alive. QUE SUERTE QUE TIENES!')
   elif friendlyCave == '2':
          print ('El melocontonton no muere y te debora el alma')
   elif friendlyCave == '3':
          print ('AJJAJAJA ganar dice eso es de noobs...')
   else:
          print('Naa.. perdiste primo, estas too burlao!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	Iniciar()
	caveNumber = EligeOpcion()
	CompruebaOpcion(caveNumber)
 	print('Quieres jugar otra vez? (y or n)')
 	playAgain = str(raw_input())
