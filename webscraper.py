from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?N=100161551%204814&cm_sp=Cat_Cell-Phones_1-_-VisNav-_-Unlocked-Cell-Phones'
#opens connection, grabs page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
#grabs each thing
containers = page_soup.findAll("div", {"class": "item-container"})
container = containers

filename = "products.csv"
f = open(filename, "w")

headers = "product_name, shipping\n"

f.write(headers)

for container in containers:	
	brand = container.findAll("a", {"img": "title"})
	title_container = container.findAll("a", {"class": "item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class": "price-ship"})
	shipping = shipping_container[0].text.strip()
	
	print("product_name: " + product_name)
	print("shipping: " + shipping)

	f.write(product_name.replace(",", "  ") + ", " + shipping + "\n")

f.close()