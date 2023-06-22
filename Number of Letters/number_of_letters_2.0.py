from collections import Counter 
import string
print("\nTotal number of letters is :  ")
with open(r"c:\Users\training.user\Documents\words.txt","r") as file:
    word = file.read().upper() #to convert so letters are counted as the same wether upper or lower
    letter_count = Counter(word)  
    sorted_letter_count = dict(sorted(letter_count.items()))
    for letter, count in sorted_letter_count.items():       
        if letter not in string.punctuation and letter not in string.digits:    #copied from number_of_letters.py
            print(f'{letter}: {count}')