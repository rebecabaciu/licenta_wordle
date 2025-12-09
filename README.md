# 🇷🇴 Wordle AI Solver & Analysis Engine

Acest proiect reprezintă componenta avansată de cercetare a lucrării de licență: **"Analiza Strategiilor Optime în jocurile de cuvinte"**.

Scopul a fost dezvoltarea și compararea unor agenți inteligenți capabili să rezolve jocul Wordle cu o eficiență supraumană, folosind tehnici de filtrare a spațiului de căutare și maximizare a informației (Greedy / Entropie).

> **Notă:** Implementarea vizuală (Frontend-ul React) care utilizează datele generate de acest proiect poate fi găsită aici: [Wordle](https://github.com/rebecabaciu/wordle)

## Arhitectura Proiectului

Sistemul este modular, având un motor de joc central și mai mulți agenți care "concurează" pentru cel mai bun scor.

### 1. Game Engine (`dfa.py`)
Un simulator complet al jocului Wordle (văzut ca un automat finit determinist) care:
* Gestionează starea jocului și validarea cuvintelor.
* Oferă feedback exact ca în jocul original (Verde, Galben, Gri).
* Permite rularea a mii de simulări în câteva secunde pentru testarea agenților.

### 2. Agenții AI (Strategiile)

Am implementat 4 niveluri de inteligență artificială pentru a demonstra evoluția performanței:

* **Agent Baseline (`agent_baseline.py`):**
    * *Strategie:* Random Guessing.
    * *Rol:* Stabilește limita de jos a performanței (noroc pur).
    * *Rata de succes:* ~0-5% (în 6 încercări).

* **Agent Determinist (`agent_determinist.py`):**
    * *Strategie:* Folosește o listă fixă de cuvinte de start optime (ex: "RAISE", "CLONE").
    * *Rol:* Testează ipoteza "cuvintelor de aur" fără adaptare la feedback.

* **Agent Eliminator (`agent_eliminator.py`):**
    * *Strategie:* Pruning (Tăiere). După fiecare feedback, elimină din dicționar toate cuvintele care nu respectă regulile impuse de indiciile primite.
    * *Performanță:* Rezolvă majoritatea jocurilor, dar nu mereu optim.

* **Agent Greedy - The Smartest (`agent_greedy.py`):**
    * *Strategie:* Analiză Pozițională & Maximizare Locală.
    * Calculează frecvența fiecărei litere pe fiecare poziție (0-4) în lista rămasă de cuvinte.
    * Alege cuvântul care are cel mai mare "Scor de Probabilitate", maximizând șansa de a nimeri litere verzi.
    * *Rata de succes:* >95% în simulări.

### 3. Data Pipeline (`main.py`)
* Script de **Web Scraping** care construiește baza de date de cuvinte.
* Extrage automat lista oficială de cuvinte Wordle folosind `BeautifulSoup` și le stochează într-o bază de date `SQLite`.


## Rezultate Obținute (Licență)
În urma simulărilor pe un eșantion de 10.000 de jocuri:
* **Baseline & Determinist:** < 1% succes
* **Eliminator:** ~98% succes
* **Greedy:** ~99% succes

---
*Acest cod a servit drept fundament experimental pentru validarea ipotezelor din lucrarea de licență.*
