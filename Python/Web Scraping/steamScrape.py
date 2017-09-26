import bs4
import time
from urllib.request import urlopen as uReq
from bs4 import Tag
from bs4 import BeautifulSoup as bs


try:
	myUrl = "http://store.steampowered.com/search/?specials=1"

	#Open url and grab page
	uClient = uReq(myUrl)
	pageHtml = uClient.read()
	uClient.close()

	#parse HTML
	pageSoup = bs(pageHtml, "html.parser")

	containers = pageSoup.findAll("a", {"class":"search_result_row"})

	filename = "./Steam/GamesByRelevanceD{}H{}.csv".format(time.strftime("%d-%m-%Y"), time.strftime("%H:%M:%S"))
	f = open(filename, "w")

	headers = "Game,Release date,Discount,Old price,Current Price\n"

	f.write(headers)

	for container in containers:
	
		nameContainer = container.findAll("span",{"class":"title"})
		gameName = nameContainer[0].text.strip()
	
		releaseContainer = container.findAll("div", {"class":"search_released"})
		releaseDate = releaseContainer[0].text.strip()

		discountContainer = container.findAll("div", {"class":"search_discount"})
		discountPerc = discountContainer[0].text.strip()

		oldCont = container.findAll("span", {"style":"color: #888888;"})
		oldPrice = oldCont[0].text

		priceContainer = container.findAll("br")
		currentPrice = priceContainer[0].text

		print("gameName: "+gameName)
		print("releaseDate: "+releaseDate)
		print("discountPerc: "+discountPerc)
		print("oldPrice: "+oldPrice)
		print("currentPrice: "+currentPrice)

		f.write("\n"+gameName+","+releaseDate+","+discountPerc+","+oldPrice.replace(",",".")+","+currentPrice.replace(",","."))

	f.close()
except:
	raise
finally:
	print("\n\n ...Done!")

