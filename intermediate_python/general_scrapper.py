import urllib.request 
from bs4 import BeautifulSoup
from  urllib.parse import urljoin
import os  

baseurl= "http://apod.nasa.gov/apod/archivepix.html" 
download_dir = "/home/rcarbone/Downloads/apod_pictures" 

to_visit = set((baseurl,))
visited = set()

while to_visit:
	current_page = to_visit.pop()
	print("visiting: ", current_page)
	visited.add(current_page)
	content = urllib.request.urlopen(current_page).read()
	# Pick a link to visit
	# Visit the link
	# Extract any new links
	for link in BeautifulSoup(content, "lxml").findAll("a"):
		absolute_link = urljoin(current_page, link["href"])
		if absolute_link not in visited:
			to_visit.add(absolute_link)
		else:
			print("Already visited: ", absolute_link)

	for img in BeautifulSoup(content, "lxml").findAll("img"):
		img_href = urljoin(current_page, img["src"])
		print("Downloading image: ", img_href)
		img_name = img_href.split("/")[-1] 
		urllib.request.urlretrieve(img_href, os.path.join(download_dir, img_name))
		
