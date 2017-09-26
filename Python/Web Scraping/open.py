from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://store.steampowered.com/search/?specials={}".format(pageN))