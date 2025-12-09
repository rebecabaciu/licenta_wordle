import math
from collections import Counter
from dfa import GameState
from words import words

# Funcția de feedback bazată pe GameState
def feedback(guess, target):
    gs = GameState(target)
    return tuple(gs.feedback(guess))

# Entropia pentru un cuvânt față de toate cuvintele
def calculeaza_entropie(guess, all_words):
    frecvente = Counter()
    for target in all_words:
        f = feedback(guess, target)
        frecvente[f] += 1

    total = len(all_words)
    entropie = 0.0
    for count in frecvente.values():
        p = count / total
        entropie -= p * math.log2(p)
    return entropie

# Rulare completă pentru toate cuvintele
def top_entropii(word_list, top_n=10):
    rezultate = []
    total = len(word_list)

    for i, guess in enumerate(word_list):
        e = calculeaza_entropie(guess, word_list)
        rezultate.append((guess, round(e, 5)))

        if (i + 1) % 100 == 0 or i == total - 1:
            print(f"Procesat: {i + 1}/{total} cuvinte")

    rezultate.sort(key=lambda x: x[1], reverse=True)

    print("\nTop cuvinte după entropie informațională:")
    for i, (cuvant, e) in enumerate(rezultate[:top_n], start=1):
        print(f"{i}. {cuvant}: {e} biți")

    return rezultate

if __name__ == "__main__":
    top_entropii(words, top_n=20)
