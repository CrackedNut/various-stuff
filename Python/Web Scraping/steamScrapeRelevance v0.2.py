from bs4 import BeautifulSoup as bs
from selenium import webdriver

while True:
	try:
		toScrape = int(input("Pages to scrape through: "))
		break
	except:
		print("\nPlease only enter whole numbers...\n\n")
		continue

browser = webdriver.PhantomJS()

for pageN in range(1,toScrape):
	print("\nScraping page {}...".format(pageN))
	try:
		#open connection, load page and pull
		browser.get("http://store.steampowered.com/search/?specials=1&page={}".format(pageN))

		#parse HTML
		pageSoup = bs(browser.page_source, "html.parser")
		
		#find all <a> which contain info.
		containers = pageSoup.findAll("a", {"class":"search_result_row"})
		
		#create a .csv for storing 
		filename = "./Steam/Games by relevance({}{}) p{}.csv".format(time.strftime("%d-%m-%Y"), time.strftime("%H:%M:%S"), pageN)
		
		#Headers for .csv
		header = "Game,Release date,Discount,Old price,Current Price\n"
		
		#Create blank .csv and write the headers
		f = open(filename, "w")
		f.write(headers)

		for container in containers:
			nameContainer = container.findAll("span",{"class":"title"})
			gameName = nameContainer[0].text.strip()

			releaseContainer = container.findAll("div", {"class":"search_released"})
			releaseDate = releaseContainer[0].text.strip()
            
            #because some items have no discount, check if discount. If none execute except blocks
			try:
				discountContainer = container.findAll("dev", {"class":"title"})
				discountPerc = discountContainer[0].text.strip()
			except:
				discountPerc = "None"

			try:
				oldContainer = container.findAll("span",{"style":"color: #888888;"})
				oldPrice = oldContainer[0].text
			except:
				oldPrice = "/"

			try:
				priceContainer = container.findAll("br")
			except:
				priceContainer = container.findAll("div",{"class":"search_price"})
			finally:
				currentPrice = priceContainer[0].text

			print("gameName: "+gameName)
			print("releaseDate: "+releaseDate)
			print("discountPerc: "+discountPerc)
			print("oldPrice: "+oldPrice)
			print("currentPrice: "+currentPrice)
			
			f.write("\n"+gameName+","+releaseDate.replace(",", " ")+","+discountPerc+","+oldPrice.replace(",", ".")+","+currentPrice.replace(",", "."))
		
		f.close()

		print("\n\nProgress: {}%".format(int((pageN/toScrape)*100.0)))
	except:
		break

print("\n\nDone!")
