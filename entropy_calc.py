import math
from collections import Counter
from dfa import GameState
from words import words

def feedback(guess, target):
    # folosim clasa ta deja implementată
    gs = GameState(target)
    return tuple(gs.feedback(guess))  # tuple ca să poată fi folosit ca cheie în Counter

def calculeaza_entropie(guess, words):
    counter = Counter()
    for target in words:
        f = feedback(guess, target)
        counter[f] += 1

    total = sum(counter.values())
    entropy = 0
    print(f"Calcul entropie pentru cuvântul: {guess}\n")
    print(f"{'Feedback':<20} {'Count':<10} {'P(f)':<10} {'-P log2 P':<10}")

    for f, count in counter.items():
        p = count / total
        term = -p * math.log2(p)
        entropy += term
        print(f"{str(f):<20} {count:<10} {round(p,5):<10} {round(term,5):<10}")

    print(f"\nEntropie totală pentru '{guess}': {round(entropy, 4)} bits")
    return entropy

# Exemplu de rulare
if __name__ == "__main__":
    calculeaza_entropie("slate", words)
