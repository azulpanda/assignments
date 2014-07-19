#-*- coding:UTF-8 -*-
import os
from urllib import urlopen
from bs4 import BeautifulSoup


data = urlopen('http://www.huffingtonpost.kr/2014/07/19').read()
soup = BeautifulSoup(data)

for title in soup.select('h3 a'):
	if not os.path.exists("07_19_2014"):
		os.makedirs("07_19_2014")

	file_name = title.text.replace('"','').replace('?','').replace('\\','').replace('/','').replace(':','').replace('*','').replace('<','').replace('>','').replace('|','')
	file_name_mode = "07_19_2014/" + file_name + ".txt"
	file = open(file_name_mode, 'w')

	new_soup = BeautifulSoup(urlopen(title["href"]).read())
	for para in  new_soup.select('#mainentrycontent p'):
		file.write(para.text.replace('"','').replace('?','').replace('\\','').replace('/','').replace(':','').replace('*','').replace('<','').replace('>','').replace('|','').encode('UTF-8'))

	file.close() 
