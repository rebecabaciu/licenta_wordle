class GameState:
    def __init__(self, word, max_attempts=6):
        self.word = word
        self.correct_letters = [""] * 5
        self.all_guessed_words = []
        self.remaining_attempts = max_attempts
        self.status = "start"

    def feedback(self, guess):
        result = [0] * 5
        used = [False] * 5
        target = list(self.word)

        # Verde
        for i in range(5):
            if guess[i] == target[i]:
                result[i] = 2
                used[i] = True

        # Galben
        for i in range(5):
            if result[i] == 0:
                for j in range(5):
                    if not used[j] and guess[i] == target[j]:
                        result[i] = 1
                        used[j] = True
                        break
        return result

    def guess(self, word):
        if self.status in ["win", "lose"]:
            return
        self.all_guessed_words.append(word)
        fb = self.feedback(word)
        if fb == [2, 2, 2, 2, 2]:
            self.status = "win"
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts <= 0:
                self.status = "lose"
            else:
                self.status = "progress"
