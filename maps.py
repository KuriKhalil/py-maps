from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os

def init_driver():
    print("Current directory: ", os.getcwd())
    PATH = "Chrome_Driver_Path"
    service = Service(PATH)
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def open_maps_page(driver, url):
    driver.get(url)

def refuse_cookies(driver):
    try:
        refuse_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Tout refuser']"))
        )
        refuse_button.click()
        print("✅ Cookies have been refused.")
    except Exception as e:
        print(f"❌ Unable to bypass cookies. Error: {str(e)}")

<<<<<<< HEAD
def show_all_reviews(driver):
    try:
        more_reviews = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Avis')]"))
        )
        more_reviews.click()
        print("✅ All reviews are displayed.")
        time.sleep(0.5)
    except Exception as e:
        print(f"❌ Unable to show all reviews. Error: {str(e)}")
        time.sleep(1)
=======
            # Mettre le lien de la page Google Maps dont vous souhaitez scraper les avis
driver.get("https://maps.app.goo.gl/Tzct1Lu134uSTdt17")#https://maps.app.goo.gl/f9NLWciRyk3Wsdjg8
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
    more_reviews = WebDriverWait(driver, 5).until(                          #\"Plus d'avis\"
       EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Avis')]"))
    )
    more_reviews.click()
    print("✅ Tous les avis sont affichés.")
    time.sleep(0.5)
except Exception as e:
    print(f"❌ Impossible de voir tous les avis. Erreur : {str(e)}")
    
    time.sleep(1)
>>>>>>> 085bb912fe66b5120d50dd37ff38d660dd0d4ac5

# Trier les avis
try:
    recent_reviews = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, ('fontBodyLarge k5lwKb') and div(@aria-label='Avis les plus pertinents')]"))
    )
    recent_reviews.click()
    print("✅ 'Le menu de tri' est ouvert.")
    time.sleep(1)

except Exception as e:
    print(f"❌ Impossible de trier les avis. Erreur : {str(e)}")


# Scrolling dans le panneau des avis
def scroll_reviews_panel(driver, max_attempts=100):
    print("Scrolling reviews in progress...")
    try:
        reviews_panel = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf')]"))
        )
        last_height = driver.execute_script("return arguments[0].scrollHeight", reviews_panel)
        no_new_content_count = 0
        max_no_new_content = 2

        for i in range(max_attempts):
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", reviews_panel)
            print(f"Scroll attempt {i+1}/{max_attempts}")
            time.sleep(0.5)

            new_height = driver.execute_script("return arguments[0].scrollHeight", reviews_panel)
            if new_height == last_height:
                no_new_content_count += 1
                if no_new_content_count >= max_no_new_content:
                    print("End of scroll - no more new content")
                    break
            else:
                no_new_content_count = 0
                last_height = new_height

            try:
                more_reviews_btn = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Plus d'avis')]"))
                )
                if more_reviews_btn.is_displayed():
                    driver.execute_script("arguments[0].click();", more_reviews_btn)
                    print("✅ Clicked on 'More reviews'")
                    time.sleep(0.5)
            except:
                pass

        print("✅ Scrolling completed successfully")

    except Exception as e:
<<<<<<< HEAD
        print(f"❌ Error during scrolling: {str(e)}")

def expand_all_reviews(driver):
    try:
        all_plus_buttons = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'w8nwRe kyuRq')]"))
        )
        for btn in all_plus_buttons:
            try:
                driver.execute_script("arguments[0].click();", btn)
                print("✅ 'More' buttons clicked")
            except:
                continue
        print(f"✅ {len(all_plus_buttons)} 'More' buttons clicked.")
    except Exception as e:
        print(f"❌ Unable to click on 'More' buttons. Error: {str(e)}")

def extract_reviews(driver):
    avis_data = []
    try:
        review_cards = driver.find_elements(By.XPATH, "//div[@data-review-id]")
        for card in review_cards:
            try:
                pseudo = card.find_element(By.CLASS_NAME, "d4r55").text
            except:
                pseudo = "[Username not found]"
=======
        print(f"❌ Erreur pendant le scroll: {str(e)}")
        

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


        except:
            continue
    
    print(f"✅ {len(all_plus_buttons)} boutons 'Plus' cliqués.")
except Exception as e:
    print(f"❌ Impossible de cliquer sur les boutons 'Plus'. Erreur : {str(e)}")
>>>>>>> 085bb912fe66b5120d50dd37ff38d660dd0d4ac5

            try:
                avis = card.find_element(By.CLASS_NAME, "MyEned").text.replace('\n', ' ')
            except:
                avis = "[No review left]"

<<<<<<< HEAD
            try:
                if card.find_element(By.XPATH, ".//span[@aria-label]").get_attribute("aria-label"):
                    note = card.find_element(By.XPATH, ".//span[@aria-label]").get_attribute("aria-label")
                else:
                    note = card.find_element(By.CLASS_NAME, "fzvQIb").text
            except:
                note = "Rating not available"
=======
try:
    review_cards = driver.find_elements(By.XPATH, "//div[@data-review-id]")
    
    for card in review_cards:
        try:
            pseudo = card.find_element(By.CLASS_NAME, "d4r55").text
        except:
            pseudo = "[Pseudo non trouvé]"
>>>>>>> 085bb912fe66b5120d50dd37ff38d660dd0d4ac5

            data = {
                "pseudo": pseudo,
                "avis": avis,
                "note": note
            }
            avis_data.append(data)
        print(f"Number of reviews retrieved: {len(avis_data)}")
        print(avis_data)
    except Exception as e:
        print(f"❌ Unable to extract reviews. Error: {str(e)}")
    time.sleep(0.5)
    return avis_data

<<<<<<< HEAD
def remove_duplicates(avis_data):
    avis_uniques = []
    seen = set()
    for avis in avis_data:
        key = (avis["pseudo"], avis["avis"], avis["note"])
        if key not in seen:
            seen.add(key)
            avis_uniques.append(avis)
    return avis_uniques
=======
        try:
            if card.find_element(By.XPATH, ".//span[@aria-label]").get_attribute("aria-label"):
                note = card.find_element(By.XPATH, ".//span[@aria-label]").get_attribute("aria-label")
            else:
                note = card.find_element(By.CLASS_NAME, "fzvQIb").text
        except:
            note = "Note non disponible"
>>>>>>> 085bb912fe66b5120d50dd37ff38d660dd0d4ac5

def save_to_csv(avis_uniques, filename="avis_data.csv"):
    if avis_uniques:
        with open(filename, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["pseudo", "avis", "note"])
            writer.writeheader()
            writer.writerows(avis_uniques)
            print(f"✅ The CSV file has been created with {len(avis_uniques)} unique entries!")
    else:
        print("No review data to save.")

<<<<<<< HEAD
if __name__ == "__main__":
    driver = init_driver()
    open_maps_page(driver, "Google_Maps_URL_here")
    refuse_cookies(driver)
    show_all_reviews(driver)
    scroll_reviews_panel(driver)
    expand_all_reviews(driver)
    avis_data = extract_reviews(driver)
    avis_uniques = remove_duplicates(avis_data)
    save_to_csv(avis_uniques)
    
=======
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
>>>>>>> 085bb912fe66b5120d50dd37ff38d660dd0d4ac5
