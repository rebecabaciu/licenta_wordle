import pandas as pd
from words import words  # ← Lista reală de cuvinte Wordle (de 5 litere)

# Funcția de feedback pentru Wordle
def feedback(guess, target):
    result = [0] * 5
    target_used = [False] * 5

    # Pas 1: Verde – literă corectă, poziție corectă
    for i in range(5):
        if guess[i] == target[i]:
            result[i] = 2
            target_used[i] = True

    # Pas 2: Galben – literă corectă, poziție greșită
    for i in range(5):
        if result[i] == 0:
            for j in range(5):
                if not target_used[j] and guess[i] == target[j]:
                    result[i] = 1
                    target_used[j] = True
                    break
    return result

# Setăm un cuvânt-țintă (poți schimba după preferință)
target_word = "stone"

# Aplicăm funcția pe toate cuvintele din listă
results = []
for guess in words:
    results.append((guess, feedback(guess, target_word)))

# Afișăm rezultatele într-un tabel
df = pd.DataFrame(results, columns=["Guess", "Feedback"])
print(df)
