from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os

print("Répertoire courant : ", os.getcwd())
# Remplacer par le chemin de votre chromedriver
PATH = "D:/Dev/2_Scaping_training/Scraping Maps/chromedriver.exe"
service = Service(PATH)

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

            # Mettre le lien de la page Google Maps dont vous souhaitez scraper les avis
driver.get("https://maps.app.goo.gl/zMzFSnPi3yGFYNMe6")

# Gestion des cookies
try:
    refuse_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Tout refuser']"))
    )
    refuse_button.click()
    print("✅ Les cookies ont bien été refusés.")
except Exception as e:
    print(f"❌ Impossible de passer les cookies. Erreur : {str(e)}")

# Voir tous les avis
try:
    more_reviews = WebDriverWait(driver, 5).until(
       EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, \"Plus d'avis\")]"))
    )
    more_reviews.click()
    print("✅ Tous les avis sont affichés.")
    time.sleep(0.5)
except Exception as e:
    print(f"❌ Impossible de voir tous les avis. Erreur : {str(e)}")

def scroll_reviews_panel(driver, max_attempts=100):
    print("Scrolling des avis en cours...")
    
    try:
        # Trouver le bon conteneur de scroll
        reviews_panel = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf')]"))
        )
        
        last_height = driver.execute_script("return arguments[0].scrollHeight", reviews_panel)
        no_new_content_count = 0
        max_no_new_content = 2
        
        for i in range(max_attempts):
            # Scrolling jusqu'en bas
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", reviews_panel)
            print(f"Scroll attempt {i+1}/{max_attempts}")
            time.sleep(0.5)
            
            # Vérifie la nouvelle hauteur
            new_height = driver.execute_script("return arguments[0].scrollHeight", reviews_panel)
            if new_height == last_height:
                no_new_content_count += 1
                if no_new_content_count >= max_no_new_content:
                    print("Fin du scroll - plus de nouveau contenu")
                    break
            else:
                no_new_content_count = 0
                last_height = new_height
                
            # Vérifie et clique sur "Plus d'avis" si présent
            try:
                more_reviews_btn = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Plus d'avis')]"))
                )
                if more_reviews_btn.is_displayed():
                    driver.execute_script("arguments[0].click();", more_reviews_btn)
                    print("✅ Cliqué sur 'Plus d'avis'")
                    time.sleep(0.5)
            except:
                pass
        
        print("✅ Scroll terminé avec succès")
        
    except Exception as e:
        print(f"❌ Erreur pendant le scroll: {str(e)}")

# Appeler la fonction de scroll
scroll_reviews_panel(driver)

# Déplier tous les textes d'avis
try:
    all_plus_buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'w8nwRe kyuRq')]"))
    )
    
    for btn in all_plus_buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            print("✅ Boutons 'Plus' cliqué")
           #time.sleep(0.5)
        except:
            continue
    
    print(f"✅ {len(all_plus_buttons)} boutons 'Plus' cliqués.")
except Exception as e:
    print(f"❌ Impossible de cliquer sur les boutons 'Plus'. Erreur : {str(e)}")

# Initialiser une liste vide pour stocker les avis
avis_data = []

try:                                              #//button[contains(@class, 'jftiEf fontBodyMedium')]
    review_cards = driver.find_elements(By.XPATH, "//div[@data-review-id]")
    
    for card in review_cards:
        try:
            pseudo = card.find_element(By.CLASS_NAME, "d4r55").text
        except:
            pseudo = "[Pseudo non trouvé]"

        try:
            avis = card.find_element(By.CLASS_NAME, "MyEned").text.replace('\n', ' ')
        except:
            avis = "[Aucun avis laissé]"

        try:
            note = card.find_element(By.XPATH, ".//span[@aria-label]").get_attribute("aria-label")
        except:
            note = "Note non disponible"

        data = {
            "pseudo": pseudo,
            "avis": avis,
            "note": note
        }
        avis_data.append(data)
                
    print(f"Nombre d'avis récupérés: {len(avis_data)}")
    print(avis_data)

except Exception as e:
    print(f"❌ Impossible d'extraire les avis. Erreur : {str(e)}")
time.sleep(0.5)

# Supprimer les doublons (par combinaison unique de pseudo + avis + note)
avis_uniques = []
seen = set()

for avis in avis_data:
    key = (avis["pseudo"], avis["avis"], avis["note"])
    if key not in seen:
        seen.add(key)
        avis_uniques.append(avis)

# Écriture dans le CSV avec les avis uniques
if avis_uniques:
    with open("avis_data.csv", mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["pseudo", "avis", "note"])
        writer.writeheader()
        writer.writerows(avis_uniques)
        print(f"✅ Le fichier CSV a bien été créé avec {len(avis_uniques)} entrées uniques !")
else:
    print("Aucune donnée d'avis à enregistrer.")