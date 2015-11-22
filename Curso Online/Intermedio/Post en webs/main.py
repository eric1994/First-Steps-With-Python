#-*- coding: utf-8 -*-
import argparse
from prct6 import WebInformation

parser = argparse.ArgumentParser(description="Tool para escanear")
parser.add_argument("-u","--url",dest="target_url",help="URL de destino",required=True)
parser.add_argument("-t","--tech",help="Extraer tecnología",action="store_true")
parser.add_argument("-r","--reverse",help="Extraer sitios del server",action="store_true")



arguments = parser.parse_args()

if arguments.tech:
	ins = WebInformation(arguments.target_url)
	technologies = ins.technologies()
	print(technologies)

if arguments.reverse:
	ins = WebInformation(arguments.target_url)
	sites = ins.reverseip()
	for x in sites:
		print(x)