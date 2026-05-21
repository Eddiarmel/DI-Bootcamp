"""
Challenge 1: Letter Index Dictionary

"""
User_word = input("Enter a word: ")
#2. Creating the Dictionary
letter_index = {}
for index, letter in enumerate(User_word):
    if letter not in letter_index:
        letter_index[letter] = [index]
    else:
        letter_index[letter].append(index)

print(letter_index)


"""
Challenge 2: Affordable Items
"""

