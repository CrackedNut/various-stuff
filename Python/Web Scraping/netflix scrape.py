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
	print("\nScraping page {}...".format(pageN))
	try:
		#open connection, load page and pull
		browser = webdriver.PhantomJS()
		browser.get("https://www.netflix.com/")

		#parse HTML
		pageSoup = bs(browser.page_source, "html.parser")
		
		#find all <div> which contain info.
		containers = pageSoup.findAll("div", {"class":"title-card-1-0"})
		
		#create a .csv for storing 
		filename = "./Netflix new/news.csv"
		
		#Headers for .csv
		headers = "Name"
		
		#Create blank .csv and write the headers
		f = open(filename, "w")
		f.write(headers)
		result=[]
		cont=0
		for tag in containers.findAll('True',{'aria-label':True}):
			result.append(tag["aria-label"])

			f.write("\n",result[cont])
			cont += 1
			print(result[cont])
		f.close()

	except:
		break

print("\n\nProgress 100%... Done!")
