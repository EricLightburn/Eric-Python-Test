import string

class LetterCounter:                       #i used a similar layout from bank account
    def __init__(self, file_path):
        self.file_path = file_path
        self.letter_counts = {}

    def count_letters(self):
        with open(self.file_path, "r") as f:    #use variable to store file path instead, to pass as arguament to open() function
            words = f.read().split()
        for word in words:
            word = word.lower()
            for letter in word:
                if letter not in self.letter_counts:
                    self.letter_counts[letter] = 0
                self.letter_counts[letter] += 1

    def display_counts(self):
        sorted_letter_counts = sorted(self.letter_counts.items(), key=lambda x: x[0])
        for letter, count in sorted_letter_counts:
            if letter not in string.punctuation and letter not in string.digits:
                print(f"{letter}: {count}")

counter = LetterCounter(r"c:\Users\training.user\Documents\words.txt")
counter.count_letters()
counter.display_counts()
