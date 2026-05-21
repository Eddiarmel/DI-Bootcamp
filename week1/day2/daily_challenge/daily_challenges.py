"""
Challenge 1: Letter Index Dictionary

"""
# User_word = input("Enter a word: ")
# #2. Creating the Dictionary
# letter_index = {}
# for index, letter in enumerate(User_word):
#     if letter not in letter_index:
#         letter_index[letter] = [index]
#     else:
#         letter_index[letter].append(index)

# print(letter_index)


"""
Challenge 2: Affordable Items
"""
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# 1. Nettoyer le portefeuille
wallet = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))
    
    if price <= wallet:
        basket.append(item) 
        wallet -= price 

if basket == []:
    print("Nothing")
else:
    print(sorted(basket))