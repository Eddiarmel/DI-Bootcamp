"""
Exercice 1 : Bonjour le monde
Instructions
Imprimez le résultat suivant en utilisant une seule ligne de code :

Hello world
Hello world
Hello world
Hello world
"""

print("hello world")
print("hello world")
print("hello world")
print("hello world")


"""Exercice 3 : Quel est le résultat ?
Instructions
Prédisez le résultat des extraits de code suivants :
indiquez votre prédiction en commentaire, puis exécutez le code et comparez.

Exemple:

>>> 15 < 8 #False
>>> 5 < 3
>>> 3 == 3
>>> 3 == "3"
>>> "3" > 3
>>> "Hello" == "hello"
"""
### solution

# 15 < 8 #False
# 5 < 3 # False
# 3 == 3 # true
# 3 == "3" # False
# "3" > 3 # False
# "Hello" == "hello" # False

"""Exercice 4 : La marque de votre ordinateur
Instructions
Créez une variable computer_branddont la valeur correspond à la marque de votre ordinateur.
À l'aide de la computer_brandvariable, affichez une phrase qui indique ce qui suit :
"I have a <computer_brand> computer."
"""
### solution
computer_brand="Dell i3"
print(f"I have a {computer_brand} computer.")

"""
🌟 Exercice 5 : Vos informations
Instructions
Créez une variable appelée name, et attribuez-lui la valeur de votre nom.
Créez une variable appelée age, et attribuez-lui la valeur de votre âge.
Créez une variable appelée shoe_size, et attribuez-lui la valeur de votre pointure.
Créez une variable infoet attribuez-lui une phrase intéressante vous concernant. Cette phrase doit contenir toutes les variables créées dans les parties 1, 2 et 3.
Faites en sorte que votre code imprime le infomessage.
Exécutez votre code.
"""
name="Kia"
age=26
hoe_size=1.70
infos=f"nom:{name} age:{age} taille:{hoe_size} m"
print(infos)

"""
 Exercice 6 : A et B
Instructions
Créez deux variables, aet b.
La valeur de chaque variable doit être un nombre.
Si al 
a valeur est supérieure à b, votre code doit afficher "Hello World".
"""
a=3
b=2
if a>b:
    print("Hello world")

"""
Exercice 7 : Pair ou impair
Instructions
Écrivez un code qui demande à l'utilisateur un nombre et détermine si ce nombre est pair ou impair.
"""
print("Bienvenue dans le calcule de nombre paire")
nombre=int(input("veuillez entrer un nombre :"))
if nombre %2==0:
    print("le nombre est paire ")
else:
    print("le nombre est impaire")

"""
Exercice 8 : Quel est votre nom ?
Instructions
Écrivez un programme qui demande à l'utilisateur son nom et vérifie 
s'il porte le même nom. Affichez un message humoristique en fonction du résultat.
"""
votre_nom=input("veuillez entrer votre Nom:")
Name="eddi"
if votre_nom.lower()==Name.lower():
    print("super ! , on na le meme Nom")
else:
    print(f"ah ! nous avons pas le meme Nom {Name}!")

"""
🌟 Exercice 9 : Être assez grand pour faire des montagnes russes
Instructions
Écrivez un code qui demandera à l'utilisateur sa taille en centimètres.
S’ils mesurent plus de 145 cm, imprimez un message indiquant qu’ils sont assez grands pour monter à cheval.
S’ils ne sont pas assez grands, imprimez un message indiquant qu’ils doivent encore grandir pour pouvoir monter à cheval.
"""

taille_utilisateur=int(input("Veuillez entrer votre taille :"))
LIMITE_TAIILE=145
if taille_utilisateur >LIMITE_TAIILE:
    print("vous etes assez grands pour monter à cheval")
else:
    print("vous devez encore grandir pour pouvoir monter à cheval.")