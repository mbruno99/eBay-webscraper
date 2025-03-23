# 🛒 eBay Web Scraper con Selenium

---

## 📌 *Introduzione*
Questo progetto è uno **script Python** che esegue web scraping su **eBay** per estrarre informazioni sugli annunci di prodotti e salvarle in un file CSV.  

---

### 🔹 *Perché eBay?*
- È un sito **popolare** con un ampio numero di prodotti e venditori.  
- Le informazioni sui prodotti sono **chiare e strutturate**.  
- **Non richiede autenticazione** per visualizzare i dati pubblici degli annunci.  

---

## ⚙️ *Strumenti e Librerie*
- **Python** 🐍  
- **Selenium** (per l'automazione del browser)  
- **CSV** (per il salvataggio dei dati)  
- **WebDriver Manager** (per gestire automaticamente il driver di Chrome)  

---

## 🤔 *Perché Selenium?*
- **eBay carica i risultati dinamicamente tramite JavaScript**.  
- Librerie, come per esempio Requests e BeautifulSoup **non possono eseguire JavaScript**, quindi non riuscirebbero a raccogliere tutti i dati.  
- **Selenium simula un vero browser**, permettendo di navigare tra le pagine e interagire con gli elementi dinamici.  

---

## 🚀 *Come Funziona*
1. L'utente inserisce un termine di ricerca (es. "RTX 3060").  
2. Il programma costruisce l'URL di ricerca su eBay.  
3. Selenium apre eBay, attende il caricamento degli annunci e raccoglie le informazioni.  
4. I dati estratti vengono salvati in un file **CSV**.  

---

## 🛠 *Requisiti*
- Python 3.x  
- **Google Chrome** installato
- ChromeDriver (installato automaticamente da WebDriver Manager)  

---

### 📌 *Librerie necessarie*  
Installa le dipendenze con il comando:
-- pip install selenium webdriver-manager

---

## 🛑 *Limitazioni*
eBay può cambiare il layout o le classi HTML, rendendo lo script non funzionante.
Lo scraping massivo può portare a blocchi temporanei da parte di eBay.

---

Questo progetto è distribuito sotto la licenza MIT.
Sviluppato da M. Bruno
