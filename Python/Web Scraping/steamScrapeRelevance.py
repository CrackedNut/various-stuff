from bs4 import BeautifulSoup as bs
from selenium import webdriver


while True:
	try:
		toScrape = int(input("Pages to scrape through: "))
		break
	except:
		print("\nPlease only enter whole numbers...\n\n")
		continue
for pageN in range(1,toScrape):
	print("Scraping page {}...".format(pageN))
	try:
		#open connection, load page and pull
		browser = webdriver.PhantomJS()
		browser.get("http://store.steampowered.com/search/?specials=1&page={}".format(pageN))
	
		#parse HTML
		pageSoup = bs(browser.page_source, "html.parser")

		containers = pageSoup.findAll("a", {"class":"search_result_row"})

		filename = "./Steam/Games by relevance p{}.csv".format(pageN)
		f = open(filename, "w")

		headers = "Game,Release date,Discount,Old price,Current Price\n"

		f.write(headers)

		for container in containers:
	
			nameContainer = container.findAll("span",{"class":"title"})
			gameName = nameContainer[0].text.strip()
	
			releaseContainer = container.findAll("div", {"class":"search_released"})
			releaseDate = releaseContainer[0].text.strip()
            
            #because some items have no discount, check if discount. If none execute except block
			try:
				discountContainer = container.findAll("div", {"class":"search_discount"})
				discountPerc = discountContainer[0].text.strip()
				oldCont = container.findAll("span", {"style":"color: #888888;"})
				oldPrice = oldCont[0].text
                priceContainer = container.findAll("br")
                currentPrice = priceContainer[0].text

            except:
            	priceContainer = container.findAll("div",{"class":"search_price"})
				currentPrice = priceContainer[0].text
				discountPerc = "None"
				oldPrice = "/"


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

print("\n\n\n\nProgress 100% ...Done!")

