from collections import Counter 

with open(r"c:\Users\training.user\Documents\words.txt","r") as file:
    word = file.read()
    letter_count = Counter(word)
    word = ', '.join(filter(str.isalpha, word))
    sorted_letter_count = dict(sorted(letter_count.items()))

    for letter, count in sorted_letter_count.items():
        print(f'{letter}: {count}')