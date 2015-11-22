# -*- coding: utf-8 -*- 
class Moto():
	def __init__(self,marca):
		#print ("Objeto creado")
		self.marca = marca

	def acelerar(self): ###IMPORTANTE PONER EL SELF PARA QUE LO COJA
		print("\n\nLa moto {} está acelerando".format(self.marca))

	def frenar(self):
		print("La moto {} está frenando".format(self.marca))


moto_de_eric = Moto("bmw")
moto_de_eric.acelerar()
moto_de_eric.frenar()

moto_de_pepe = Moto("sosa")
moto_de_pepe.acelerar()
moto_de_pepe.frenar()