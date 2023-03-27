
import requests
from bs4 import BeautifulSoup

# URL du site web à scrapper
url = "https://bsbstore.fr/collections/vetements-hf"

# Envoi de la requête HTTP au site web et récupération du contenu HTML
response = requests.get(url)
if response.status_code == 200:
    content = response.content
else:
    print("Erreur de requête : {}".format(response.status_code))
    content = None

# Analyse du contenu HTML à l'aide de BeautifulSoup
if content is not None:
    soup = BeautifulSoup(content, 'html.parser')

    # Récupération de toutes les balises 'a' contenant des liens
    links = soup.find_all('a')

    # Parcours des liens et affichage de leur contenu
    for link in links:
        print(link.text)
else:
    print("Impossible de récupérer le contenu HTML.")
