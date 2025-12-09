import random
from collections import Counter, defaultdict
from words import words
from dfa import GameState

# Preluăm doar cuvintele de 5 litere
words = [w for w in words if len(w) == 5]

# Calculăm frecvențele literelor pe fiecare poziție (0 - 4)
pozitii_frecventa = [Counter() for _ in range(5)]
for word in words:
    for i, litera in enumerate(word):
        pozitii_frecventa[i][litera] += 1

# Funcție pentru scorul unui cuvânt pe baza frecvențelor pe poziții
def scor_cuvant(word):
    scor = 0
    litere_vazute = set()
    for i, litera in enumerate(word):
        if litera not in litere_vazute:  # nu dublăm literele
            scor += pozitii_frecventa[i][litera]
            litere_vazute.add(litera)
    return scor

def agent_greedy_guess_word(target):
    posibilitati = words.copy()
    game = GameState(target)

    while game.status not in ["win", "lose"]:
        # Calculăm scorurile cuvintelor din lista curentă
        scoruri = [(w, scor_cuvant(w)) for w in posibilitati]
        scoruri.sort(key=lambda x: x[1], reverse=True)

        guess = scoruri[0][0]
        game.guess(guess)

        # Obținem feedback și eliminăm cuvintele incompatibile
        fb = game.feedback(guess)
        noua_lista = []
        for w in posibilitati:
            if feedback(w, guess) == fb:
                noua_lista.append(w)
        posibilitati = noua_lista if noua_lista else posibilitati

    return game.status

# Funcție de testare
def test_agent_greedy(n=100):
    succes = 0
    for _ in range(n):
        target = random.choice(words)
        if agent_greedy_guess_word(target) == "win":
            succes += 1
    print(f"Agent Greedy - Succes: {succes} / {n} ({(succes / n) * 100:.2f}%)")

# Funcție pentru simularea feedbackului între două cuvinte
def feedback(cuvant, guess):
    rezultat = [0] * 5
    cuvant_list = list(cuvant)
    guess_list = list(guess)
    used = [False] * 5

    # Verde
    for i in range(5):
        if guess_list[i] == cuvant_list[i]:
            rezultat[i] = 2
            used[i] = True

    # Galben
    for i in range(5):
        if rezultat[i] == 0:
            for j in range(5):
                if not used[j] and guess_list[i] == cuvant_list[j]:
                    rezultat[i] = 1
                    used[j] = True
                    break

    return rezultat

if __name__ == "__main__":
    test_agent_greedy(100)
