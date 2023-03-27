
import requests
from bs4 import BeautifulSoup

# URL du site web à scrapper
url = "https://bsbstore.fr/collections/vetements-hf"

# Envoi de la requête HTTP au site web et récupération du contenu HTML
response = requests.get(url)
content = response.content

# Analyse du contenu HTML à l'aide de BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Récupération de toutes les balises 'a' contenant des liens
links = soup.find_all('a')

# Parcours des liens et affichage de leur contenu
for link in links:
    print(link.text)
