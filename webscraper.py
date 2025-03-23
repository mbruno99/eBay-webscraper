import csv
from urllib.parse import quote_plus

from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore



# Configurazione opzioni di Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Esegue Chrome in modalità nascosta
chrome_options.add_argument("--disable-gpu")  # Evita problemi grafici
chrome_options.add_argument("--no-sandbox")  # Evita problemi di permessi in Linux

# Installazione e avvio di ChromeDriver
# Aggiornamento automatico con webdriver-manager di chromedriver.exe
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Genera URL eBay per la ricerca
user_input = input("Cosa vuoi cercare su Ebay? ").lower().strip()
ebay_url = f"https://www.ebay.it/sch/i.html?_nkw={quote_plus(user_input)}"

# Stampa URL trovato
print(f"URL: {ebay_url}")

# Prende nome file csv
user_csv = input("Nome file csv per il salvataggio dei dati: ")
csv_file = f"{user_csv}.csv"

# Apre eBay
driver.get(ebay_url)

# Stampa il titolo della pagina
print(driver.title)

# Aspetta che almeno un elemento valido venga caricato
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "s-item"))
)

dati = []

# Tutte le inserzioni della pagina
products = driver.find_elements(By.CLASS_NAME, "s-item") # iterable

# Tutte le info delle inserzioni
for product in products:
    # Estrae il titolo dell'inserzione
    try:
        title = product.find_element(By.CLASS_NAME, "s-item__title").text
        title = title.lower().replace("nuova inserzione", "").strip()
    except NoSuchElementException:
        continue  # Salta questo elemento se il titolo non esiste
    

    # Estrae il prezzo dell'inserzion
    try:
        price = product.find_element(By.CLASS_NAME, "s-item__price").text
    except NoSuchElementException:
        price = "N/A"
    
    # Estrae la condizione e il tipo di venditore
    try:
        secondary_info = product.find_element(By.CLASS_NAME, "s-item__subtitle").text
        parts = secondary_info.split("|")


        condition = parts[0] if len(parts) > 0 else "N/A"
        vendor_type = parts[1] if len(parts) > 1 else "N/A"
    except NoSuchElementException:
        condition = "N/A"
        vendor_type = "N/A"
    

    # Estrae il nome del venditore, il numero di feedback e la percentuale del feedback
    try:
        seller_info = product.find_element(By.CLASS_NAME, "s-item__seller-info-text").text
        parts = seller_info.split(" ")

        seller_name = parts[0] if len(parts) > 0 else "N/A"
        n_feedback = parts[1].replace("(", "").replace(")", "") if len(parts) > 1 else "N/A"
        feedback_perc = parts[2] if len(parts) > 2 else "N/A"
    except NoSuchElementException:
        seller_name = "N/A"
        n_feedback = "N/A"   
        feedback_perc = "N/A"
    

    dati.append({"title":title, 
                 "price":price,
                "condition":condition.strip(), 
                "vendor_type":vendor_type.strip(), 
                "seller_name":seller_name, 
                "n_feedback":n_feedback, 
                "feedback_perc":feedback_perc})


# Salva i dati in un file csv
with open(csv_file, "w", newline="", encoding="utf-8", errors="replace") as file:
    fieldnames = ["title","price","condition","vendor_type","seller_name","n_feedback","feedback_perc"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for dato in dati:
        writer.writerow(dato)
    print("✅ File CSV salvato!")


# Chiude il browser
driver.quit()