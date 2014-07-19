#-*- coding:UTF-8 -*-
import os
import urllib
from bs4 import BeautifulSoup

def validate(text):
	return text.replace('?','').replace('\\','').replace('/','').replace(':','').replace('*','').replace('<','').replace('>','').replace('|','')

def search(keyword, disp):
	key = "e44e57b54916ee77fe547c37587ad9be"
	query = str(keyword)
	start = 1
	display = disp
	target = "news"
	url = "http://openapi.naver.com/search?key=%s&query=%s&target=%s&start=%d&display=%d" % (key, query, target, start, display)

	if not os.path.exists(query):
		os.makedirs(query)

	result = urllib.urlopen(url)
	data = result.read()

	with open(query+"/search.html", "w") as search_file:
		search_file.write(data)

	soup = BeautifulSoup(data)
	for item in soup.select("item"):
		# item_soup = BeautifulSoup(item)
		link = item.select("link")[0].text
		title = validate(item.select("title")[0].text)
		new_url = urllib.urlopen(link)
		new_data = new_url.read()
		with open(query+"/"+title+".html", "w") as file:
			file.write(new_data)
	

search("like lion", 20)