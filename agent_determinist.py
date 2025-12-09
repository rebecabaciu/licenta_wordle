# agent_determinist.py

import random
from words import words
from dfa import GameState

# Lista fixă de cuvinte prestabilite – se pot ajusta după preferință
cuvinte_fixate = ["raise", "clone", "dusty", "brick", "glyph", "vodka"]

def agent_determinist_guess_word(target):
    game = GameState(target)
    for guess in cuvinte_fixate:
        if game.status in ["win", "lose"]:
            break
        game.guess(guess)
    return game.status

def test_agent_determinist(n):
    success = 0
    for _ in range(n):
        target = random.choice(words)
        if agent_determinist_guess_word(target) == "win":
            success += 1
    print(f"Agent Determinist - Succes: {success} / {n} ({success / n:.2%})")

if __name__ == "__main__":
    test_agent_determinist(100000)
