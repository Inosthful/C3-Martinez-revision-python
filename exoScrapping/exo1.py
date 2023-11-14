# import requests
# from bs4 import BeautifulSoup


# response = requests.get("https://www.scrapethissite.com/pages/simple/")
# print(response)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')

       
#     liste_pays = soup.select('.country-container h3')

        
#     for pays in liste_pays:
#         nom_pays = pays.text
#         print(nom_pays)
# else:
#     print(f"Erreur lors de la récupération de la page. Code d'erreur : {response.status_code}")
    


import requests
from bs4 import BeautifulSoup

def scraper_pays_et_capitales(url):
 
    response = requests.get(url)

    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')

        
        liste_infos = soup.find_all('div', class_='country')

        
        for infos in liste_infos:
    
            nom_pays_element = infos.find('h3', class_="country-name")
            if nom_pays_element:
                nom_pays = nom_pays_element.text
            else:
                nom_pays = "Nom du pays non trouvé"

            capitale_element = infos.find('span', class_='country-capital')
            if capitale_element:
                capitale = capitale_element.text
            else:
                capitale = "Capitale non trouvée"
            print(f"Pays : {nom_pays} ")
            print(f"Capital : {capitale}")


url_page = 'https://scrapethissite.com/pages/simple/'
scraper_pays_et_capitales(url_page)