# Défi 1
# Demandez à l'utilisateur un numberet un length.
# Créez un programme qui affiche une liste de multiples 
# du nombre jusqu'à ce que la longueur de la liste atteigne la longueur spécifiée.

# solution

number = int(input("Entrez un nombre : "))
length = int(input("Entrez la longueur : "))
multiples = []
for i in range(1, length + 1):
    multiples.append( i*number)
print(multiples)

# solution 

"""
Défi 2
Écrivez un programme qui demande une chaîne de caractères 
à l'utilisateur et affiche une nouvelle chaîne sans les lettres consécutives identiques.
"""

mots= input("Entrez un mot : ")
resultat = ""
for lettre in mots:
    if resultat == "" or lettre != resultat[-1]:
        resultat += lettre
print(resultat)