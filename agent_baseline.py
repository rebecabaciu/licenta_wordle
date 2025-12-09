# agent_baseline.py

import random
from words import words  # Lista de 5 litere validă
from dfa import GameState  # Motorul de joc

def agent_baseline_guess_word(target):
    game = GameState(target)
    for _ in range(6):  # Wordle permite 6 încercări
        guess = random.choice(words)
        game.guess(guess)
        if game.status == "win":
            break
    return game.status

def test_agent_baseline(n):
    success = 0
    for _ in range(n):
        target_word = random.choice(words)
        result = agent_baseline_guess_word(target_word)
        if result == "win":
            success += 1
    print(f"Agent Baseline - Succes: {success} / {n} ({success / n:.2%})")

if __name__ == "__main__":
    test_agent_baseline(10000)
