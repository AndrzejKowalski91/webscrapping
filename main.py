import requests
from bs4 import BeautifulSoup
url = "https://www.pepper.pl/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

# ekstrakcja tekstu z paragrafów
paragraphs = soup.find_all('p')
print("to jest teskt z paragrafów:")
for p in paragraphs:
    print(p.text)

# obrazki z url
images = soup.find_all('img')
print("to jest img url:")
for img in images:
    print(img['src'])

# dane z  tabeli
table = soup.find('table')
rows = table.find_all ('tr')
print("\ntable dane:")
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        print(cell.text)

#element css
elements = soup.find_all(class_ = 'moja klasa')
print("\nElements z klasa 'moja klasa'")
for element in elements:
    print(element.text)