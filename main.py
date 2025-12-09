import requests
import sqlite3
from bs4 import BeautifulSoup
import time
import os
import string

# Ștergem baza de date existentă
if os.path.exists("wordle_words.db"):
    os.remove("wordle_words.db")

# Configurăm baza de date
conn = sqlite3.connect("wordle_words.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE
    )
""")
conn.commit()

def extrage_cuvinte(url):
    """Extrage cuvintele dintr-o pagină WordUnscrambler"""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Eroare la încărcarea paginii: {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Căutăm headingul corect
    headings = soup.find_all(["h1", "h2", "h3"])
    start_point = None
    for heading in headings:
        if heading.text.strip().startswith("List of Wordle words starting with"):
            start_point = heading
            break

    if not start_point:
        print("Nu am găsit titlul potrivit.")
        return []

    # După heading vine div-ul sau table-ul cu linkuri
    container = start_point.find_next("div")
    if not container:
        print("Nu am găsit containerul cu lista de cuvinte.")
        return []

    lista_cuvinte = []
    for link in container.find_all("a"):
        cuvant = link.text.strip()
        if len(cuvant) == 5 and cuvant.isalpha():
            lista_cuvinte.append(cuvant.lower())

    return lista_cuvinte

def salveaza_in_baza_de_date(cuvinte):
    """Salvează cuvintele extrase în SQLite"""
    for cuvant in cuvinte:
        try:
            c.execute("INSERT INTO words (word) VALUES (?)", (cuvant,))
        except sqlite3.IntegrityError:
            pass  # Evită duplicatele
    conn.commit()

# Iterăm prin toate literele alfabetului
for litera in string.ascii_lowercase:
    url = f"https://wordunscrambler.me/wordle-words-starting-with/{litera}"
    print(f"Procesăm: {url}")
    cuvinte = extrage_cuvinte(url)
    if cuvinte:
        salveaza_in_baza_de_date(cuvinte)
        print(f"Am găsit {len(cuvinte)} cuvinte pentru litera '{litera}'.")
    else:
        print(f"Nu am găsit cuvinte pentru litera '{litera}'.")
    time.sleep(1)  # Pauză să nu ne blocheze site-ul

print("Proces complet!")
conn.close()
