urls_list = []

print("URL: ")
print("Escribe 'hecho' si no quieres agregar mas URLS")

while True:
	item = input("> ")

	if item == "hecho":
		break
	urls_list.append(item)
	print("Added : {}".format(item))
	continue
print("Todas las URLS: ")
print(urls_list)

