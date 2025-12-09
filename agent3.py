import random
from words import words
from dfa import GameState

def filtreaza_cuvinte(candidati, incercare, feedback_primita):
    filtrati = []
    for cuv in candidati:
        gs_temp = GameState(cuv)
        fb = gs_temp.feedback(incercare)
        if fb == feedback_primita:
            filtrati.append(cuv)
    return filtrati

def agent_eliminator_guess_word(cuvant):
    candidati = words.copy()
    game = GameState(cuvant)

    # Încercăm cuvântul fix 'raise' la început
    primul = "raise"
    if primul in candidati:
        fb = game.feedback(primul)
        game.guess(primul)
        candidati = filtreaza_cuvinte(candidati, primul, fb)

    # Continuăm cu restul logicii standard
    while game.status not in ["win", "lose"]:
        if not candidati:
            break
        incercare = random.choice(candidati)
        fb = game.feedback(incercare)
        game.guess(incercare)
        candidati = filtreaza_cuvinte(candidati, incercare, fb)

    return game.status

def test_agent_eliminator(n):
    castiguri = 0
    for _ in range(n):
        target = random.choice(words)
        if agent_eliminator_guess_word(target) == "win":
            castiguri += 1
    rata = castiguri / n
    print(f"Agent Eliminator - Succes: {castiguri} / {n} ({rata:.2%})")

if __name__ == "__main__":
    test_agent_eliminator(1000)
