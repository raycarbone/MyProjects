# From the archive, follow each lionk, find the image in that linked page, and download the image.
# Parsing stuff out of html.
# Library in the std lib about downloading => urlib
# Parsing stuff out => BeuetifulSoup
import urllib.request
from bs4 import BeautifulSoup
from  urllib.parse import urljoin
import os

baseurl= "http://apod.nasa.gov/apod/archivepix.html"
download_dir = "/home/rcarbone/Downloads/apod_pictures"
content = urllib.request.urlopen(baseurl).read()

for link in BeautifulSoup(content, "lxml").findAll("a"):
	print("Follow link", link)
	href = urljoin(baseurl, link["href"])
	
	content = urllib.request.urlopen(href).read()
	for img in BeautifulSoup(content, "lxml").findAll("img"):
		img_href = urljoin(href, img["src"])
		print("Downloadimg image: ", img_href)
		img_name = img_href.split("/")[-1]
		urllib.request.urlretrieve(img_href, os.path.join(download_dir, img_name))

# Download the index page
# for each link on the index page:
#   Follow the link and pull down the image on that linked page





