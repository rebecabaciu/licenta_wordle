from collections import Counter
from words import words

def calculeaza_scor(cuvant, words):
    position_frequencies = [Counter() for _ in range(5)]

    # Pas 1: Calculează frecvențele literelor pe fiecare poziție
    for word in words:
        for i, litera in enumerate(word):
            position_frequencies[i][litera] += 1

    # Pas 2: Calculează scorul pentru cuvântul dat
    scor = 0
    print(f"\nScor pozițional pentru cuvântul: '{cuvant}'\n")
    print(f"{'Poziție':<10} {'Literă':<10} {'Frecvență':<10}")
    print("-" * 30)

    for i, litera in enumerate(cuvant):
        freq = position_frequencies[i][litera]
        scor += freq
        print(f"{i:<10} {litera:<10} {freq:<10}")

    print(f"\nScor total pentru '{cuvant}': {scor}")
    return scor

# Exemplu de rulare
if __name__ == "__main__":
    cuvant_test = "slate"
    calculeaza_scor(cuvant_test, words)
