from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import navigateur
import datetime
import time

e = datetime.datetime.now()
timeforcsv = e.strftime("%d-%m-%Y %HH%M")

def ecrire_dans_csv_ligne(nouvelle_ligne) : # liste ou string
	with open(file_name, mode='a', newline='', encoding='utf-8') as fichier:
		writer = csv.writer(fichier, delimiter=';')
    	# Écrire la nouvelle ligne dans le fichier CSV
		writer.writerow(nouvelle_ligne)

def find_accept_cookie():
	button = navigateur.driver.find_elements(By.XPATH, "//button[@type='button' and text()='OK']")
	button[0].click()

def next_page():
	global page_suivante
	page_suivante = navigateur.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@aria-label='Suivant']")))
	# print(next_page[0].get_attribute("href"))
	if len(page_suivante) !=0 :
		print("Page suivante")
		return True
	else :
		print("pas de page suivante")
		return False

def find_airbnb():
	# navigateur.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='card-container']")))
	airbnb = navigateur.driver.find_elements(By.XPATH, "//div[@data-testid='card-container']")
	for i in airbnb :
		ligne = []
		# print(i.text)
		link = i.find_element(By.XPATH, ".//a[@href]")
		# print(link.get_attribute("href"))
		base_url = extract_base_url(link.get_attribute("href"))
		print(base_url)
		ligne.append(base_url)
		airbnb_Lyon.append(link.get_attribute("href"))
		ecrire_dans_csv_ligne(ligne)
		return link.get_attribute("href")


def extract_base_url(url):
    return url.split('?')[0]


# utilisation de filtre sur le prix pour réduire le nombre de résultat :
# https://www.airbnb.fr/s/Lyon/homes?&price_min=150&price_max=160
min = (range(0, 250, 10))
max = (range(11, 251, 10))

url_to_scrap = ("https://www.airbnb.fr/s/Lyon/homes?&price_min="+str(min)+"&price_max="+str(max))

# creer une liste pour chaque collones du fichier csv :
file_name = f"{timeforcsv}_airbnb.csv"
titres = ["URL"]
ecrire_dans_csv_ligne(titres)
airbnb_Lyon = []


URLS_TO_SCRAPP = []
min_values = range(15, 99, 1)
max_values = range(16, 100, 1)
for min_val, max_val in zip(min_values, max_values):
    url_to_scrap = "https://www.airbnb.fr/s/Lyon/homes?&price_min=" + str(min_val) + "&price_max=" + str(max_val) + "&pagination_search=true&l2_property_type_ids[]=1&l2_property_type_ids[]=3"
    URLS_TO_SCRAPP.append(url_to_scrap)
min_values = range(100, 248, 2)
max_values = range(102, 250, 2)
for min_val, max_val in zip(min_values, max_values):
    url_to_scrap = "https://www.airbnb.fr/s/Lyon/homes?&price_min=" + str(min_val) + "&price_max=" + str(max_val) + "&pagination_search=true&l2_property_type_ids[]=1&l2_property_type_ids[]=3"
    URLS_TO_SCRAPP.append(url_to_scrap)
# pour les dernières pages augmentation des ranges
min_values = range(250, 495, 5)
max_values = range(255, 500, 5)
for min_val, max_val in zip(min_values, max_values):
    url_to_scrap = "https://www.airbnb.fr/s/Lyon/homes?&price_min=" + str(min_val) + "&price_max=" + str(max_val) + "&pagination_search=true&l2_property_type_ids[]=1&l2_property_type_ids[]=3"
    URLS_TO_SCRAPP.append(url_to_scrap)
# pour les dernières pages augmentation des ranges
min_values = range(500, 990, 10)
max_values = range(510, 1000, 10)
for min_val, max_val in zip(min_values, max_values):
    url_to_scrap = "https://www.airbnb.fr/s/Lyon/homes?&price_min=" + str(min_val) + "&price_max=" + str(max_val) + "&pagination_search=true&l2_property_type_ids[]=1&l2_property_type_ids[]=3"
    URLS_TO_SCRAPP.append(url_to_scrap)
# pour les dernières pages augmentation des ranges
min_values = range(1000, 1950, 50)
max_values = range(1050, 2000, 50)
for min_val, max_val in zip(min_values, max_values):
    url_to_scrap = "https://www.airbnb.fr/s/Lyon/homes?&price_min=" + str(min_val) + "&price_max=" + str(max_val) + "&pagination_search=true&l2_property_type_ids[]=1&l2_property_type_ids[]=3"
    URLS_TO_SCRAPP.append(url_to_scrap)
# pour les dernières pages augmentation des ranges
min_values = range(2000, 4900, 100)
max_values = range(2100, 5000, 100)
for min_val, max_val in zip(min_values, max_values):
    url_to_scrap = "https://www.airbnb.fr/s/Lyon/homes?&price_min=" + str(min_val) + "&price_max=" + str(max_val) + "&pagination_search=true&l2_property_type_ids[]=1&l2_property_type_ids[]=3"
    URLS_TO_SCRAPP.append(url_to_scrap)

url_to_scrap = ("https://www.airbnb.fr/s/Lyon/homes")



if __name__ == "__main__":

	navigateur.ouvrir_session_chrome()
	navigateur.driver.get(url_to_scrap)
	time.sleep(5)
	find_accept_cookie()
	time.sleep(5)
	cookies = navigateur.driver.get_cookies()

	cookie_dict = {}
	for cookie in cookies:
		cookie_dict[cookie['name']] = cookie['value']
	


	for x in URLS_TO_SCRAPP:
		navigateur.driver.get(x)
		print(f"je scrapp l'URL suivante : {x}")
		time.sleep(4)
		link = find_airbnb()
		while next_page() != False :
			page_suivante[0].click()
			time.sleep(3)
			find_airbnb()


	navigateur.fermer_session_chrome()