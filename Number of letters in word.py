from collections import Counter
my_file = open(r"c:\Users\training.user\Downloads\wordz\words.txt", "r")
counter = Counter(my_file.read())
counter['a']
print("NUMBER OF LETTERS FROM MOST TO LEAST: \n \n \n \n \n" + str(counter))
