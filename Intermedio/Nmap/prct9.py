import nmap


host_victima = "192.168.1.131"
argumentos = '-sV -p21'
escaneo = nmap.PortScanner()
escaneo.scan(hosts=host_victima, arguments=argumentos)
resultado = escaneo['192.168.1.131']['tcp'][int(21)]
print(escaneo.command_line())
for keys in resultado.keys():
	datos = keys + ": " + resultado[keys]
	print(datos)