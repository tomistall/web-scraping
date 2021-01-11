from bs4 import BeautifulSoup
from urllib.request import urlopen

#print("Hello world!")

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#Parse the url and retrieve text only - no HTML
print(soup.get_text())
#print(soup.find_all("img"))
#print(soup.title)
#print(soup.title.string)