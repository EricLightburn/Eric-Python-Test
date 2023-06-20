import string
import collections
with open(r"c:\Users\training.user\Documents\words.txt", "r") as f:
    words = f.read().split()
letter_counts = {}
for word in words:
    word = word.lower()
    for letter in word:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[0])
for letter, count in sorted_letter_counts:
    if letter not in string.punctuation and letter not in string.digits:
        print(f"{letter}: {count}")