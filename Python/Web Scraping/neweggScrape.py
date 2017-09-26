import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"
#opens connection and grabs the page
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()

# html parsing
pageSoup = soup(pageHtml, "html.parser")

#grabs each product
containers = pageSoup.findAll("div", {"class":"item-container"})


filename = "./Newegg/products.csv"
headers = "Brand,Shipping,Product name \n"

f = open(filename, "w")
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	
	shipContainer = container.findAll("li", {"class":"price-ship"})
	shipCost = shipContainer[0].text.strip()

	titleContainer = container.findAll("a", {"class":"item-title"})
	productName = titleContainer[0].text



	print("brand: " + brand)
	print("shipCost: " + shipCost)
	print("productName: " + productName)

	f.write("\n" + brand + "," + shipCost + "," + productName.replace(",", "|") + "\n")

f.close()

