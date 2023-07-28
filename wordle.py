from math import remainder
from letter_state import LetterState


class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    VOIDED_LETTER = "*"

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()
        result = [LetterState(x) for x in word]
        remaining_secret = list(self.secret)

        # Check for correct letters (GREEN)
        for i, letter in enumerate(result):
            if letter.character == self.secret[i]:
                letter.is_in_position = True
                remaining_secret[i] = self.VOIDED_LETTER

        # Check for existing but misplaced letters (YELLOW)
        for i, letter in enumerate(result):
            if not letter.is_in_position and letter.character in remaining_secret:
                index = remaining_secret.index(letter.character)
                remaining_secret[index] = self.VOIDED_LETTER
                letter.is_in_word = True

        return result


    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
