from collections import Counter 

with open(r"c:\Users\training.user\Documents\words.txt","r") as file:
    word = file.read()
    letter_count = Counter(word)
    print(letter_count)