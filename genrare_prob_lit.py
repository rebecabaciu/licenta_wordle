from words import words
from collections import Counter

# Filtrăm doar cuvintele de 5 litere (siguranță)
cuvinte = [w for w in words if len(w) == 5]

# Concatenăm toate literele și numărăm frecvențele
toate_literele = "".join(cuvinte)
frecvente = Counter(toate_literele)
total = sum(frecvente.values())

# Calculăm probabilitățile
probabilitati = {litera: frec / total for litera, frec in frecvente.items()}
probabilitati = dict(sorted(probabilitati.items(), key=lambda x: x[1], reverse=True))  # DESC

# Scriem tabelul LaTeX
with open("probabilitati_litere_wordle.tex", "w", encoding="utf-8") as f:
    f.write("\\begin{tabular}{|c|c|}\n")
    f.write("\\hline\n")
    f.write("Literă & Probabilitate \\\\\n")
    f.write("\\hline\n")
    for litera, p in probabilitati.items():
        f.write(f"{litera} & {p:.5f} \\\\\n")
    f.write("\\hline\n")
    f.write("\\end{tabular}\n")

print("Tabelul a fost generat: probabilitati_litere_wordle.tex")
