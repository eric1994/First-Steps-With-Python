import requests
from bs4 import BeautifulSoup

class WebInformation():
	def __init__(self,url):
		self.url = url
	def reverseip(self):
		if self.url.startswith("http://"):
			target_url = self.url.replace("http://","")
		else:
			target_url = self.url
		data = {"remoteHost":target_url}
		#print ("Tardo antes de la coneccion?")

		con = requests.post(
			url="http://www.ipfingerprints.com/scripts/getReverseIP.php",
			data = data
		)

		#print("Tardo despues")
		soup = BeautifulSoup(con.text, 'html.parser')
		response = list()
		#print("Ya tengo la respuesta ahora solo imprimir")
		for link in soup.find_all("a"):
			current_link = link.get("href")
			response.append(current_link[11:-2])
		return response

	def technologies(self):
		if not self.url.startswith("http://"):
			if self.url.startswith("www"):
				self.url = "http://"+self.url
			elif not self.url.startswith("www"):
				self.url ="http://www."+self.url
			else:
				return "Bad Url"
		con = requests.get(url=self.url)
		headers = con.headers.get("Server")
		#print("Header es.. {} ".format(headers))
		return headers