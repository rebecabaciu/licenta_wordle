import sqlite3

# Conectare la baza de date
conn = sqlite3.connect("wordle_words.db")
c = conn.cursor()

# Selectăm toate cuvintele
c.execute("SELECT word FROM words")
wordss = [row[0] for row in c.fetchall()]
conn.close()

# Scriem într-un fișier TypeScript
with open("wordsList.ts", "w", encoding="utf-8") as f:
    f.write("export const words: string[] = [\n")
    for wordd in wordss:
        f.write(f'    "{wordd}",\n')
    f.write("];\n")
