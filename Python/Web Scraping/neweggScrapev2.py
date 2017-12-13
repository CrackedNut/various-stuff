import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

print("Scraping... \n")

#.csv storing results
filename =  "./Newegg/scrapedVideoCards_{}_{}.csv".format(time.strftime("%d-%m-%Y"), time.strftime("%H:%M:%S"))
headers = "Product,Manufacturer,Price,Shipping"
f = open(filename, "w")
f.write(headers)

#opens connection to page and gets source
browser = webdriver.PhantomJS()
browser.get("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38")

#parse html
pageSoup = bs(browser.page_source, "html.parser")

#find all products
containers = pageSoup.findAll("div", {"class":"item-container"})

try:
	for container in containers:

		pname = container.findAll("a", {"class":"item-title"})[0].text

		try:
			manufacturer = containers.findAll("a",{"class":"item-brand"})[0].img["title"]
		except:
			manufacturer = "Unknown" 

		price = "$"+container.findAll("li",{"class":"price-current"})[0].strong.text.replace("'","")+container.findAll("li",{"class":"price-current"})[0].sup.text.replace("'","")

		shipping = container.findAll("li",{"class":"price-ship"})[0].text.strip()

		if len(shipping) == 0:
			shipping = "unknown"

		f.write("\n{},{},{},{}".format(pname.replace(",",""),manufacturer.replace(",",""),price.replace(",",""),shipping.replace(",","")))

except Exception as e:
	raise e

finally:
	f.close()