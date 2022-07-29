from bs4 import BeautifulSoup
import requests
import lxml

def get_link_data(url):
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"en",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    # print(soup.prettify())

    # Busca el nombre por la etiqueta 'producTitle'
    name = soup.select_one(selector="#productTitle").getText()
    # ELimina los espacios en blanco antes y despues de la cadena contenida en la variable 'name'
    name = name.strip()

    price = soup.find_all("span", "a-offscreen")[0]
    price = str(price)
    price = price[29:]
    price = float(price[:-7])

    return name, price