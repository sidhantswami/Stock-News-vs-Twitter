import requests
import urllib.request
import time
import re
import string
from unicodedata import normalize
from bs4 import BeautifulSoup


class FoxScraper:
	URL = "https://www.marketwatch.com/latest-news?mod=top_nav"

	def __init__(self, newsType):
		self.newsType = newsType

	def setURL(self):

		if self.newsType == "MarketWatch":
			FoxScraper.URL = "https://www.marketwatch.com/latest-news?mod=top_nav"


	def grabTicker(self):
		response = requests.get(FoxScraper.URL)

		soup = BeautifulSoup(response.text, "html.parser")

		finder = soup.find(class_="group group--headlines")

		ticker = ""

		for tag in finder.find_all("div"):

			ticker_tag = tag.find(class_="ticker__symbol")
			if ticker_tag is not None:
				#found the tag
				ticker = ticker_tag.string
				break





		return ticker


	def grabLink(self):
		response = requests.get(FoxScraper.URL)

		soup = BeautifulSoup(response.text, "html.parser")

		finder = soup.find(class_="group group--headlines")

		ticker = ""

		link_tag = ""

		for tag in finder.find_all("div"):

			ticker_tag = tag.find(class_="ticker__symbol")
			if ticker_tag is not None:
				#found the tag
				link_tag = (tag.find_all('h3'))

				break


		return ((link_tag[0].find_all('a'))[0]).get('href')










def findText(link):
	response = requests.get(link)

	soup = BeautifulSoup(response.text, "html.parser")

	finder = soup.find(id="article-meat")

	text = ""

	for tag in finder.find_all("p"):
		line = tag.contents

		a_start = 0
		a_end = 0
		found = False


		for char in line:

			if char.find("<a") != -1:
				line.remove(char)




		for newsLine in line:

			text += str(newsLine)

	text = text.replace("&apos","'",)


	return text

def findTitle(link):
	response = requests.get(link)

	soup = BeautifulSoup(response.text, "html.parser")

	finder = soup.find(class_="headline")

	title = finder.contents

	return title

# default is just the main headline
def getArticle():
	link = FoxScraper("MarketWatch")

	#print(link.newsType)
	link.setURL()
	#print(link.grabTicker())

	return findText(link.grabLink())


def getTicker():
	link = FoxScraper("MarketWatch")

	#print(link.newsType)
	link.setURL()
	return link.grabTicker()

#print(getTicker())

#print(getArticle())




