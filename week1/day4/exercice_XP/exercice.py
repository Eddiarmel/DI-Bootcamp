# Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Step 1: Create the Siamese class 
class Siamese(Cat):
    pass  


# Step 2: Create a list of cat instances 
bengal_obj = Bengal("Bengal", 3)
chartreux_obj = Chartreux("Chartreux", 5)
siamese_obj = Siamese("Siamese", 2)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance called sara_pets, passing the all_cats list
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()

# 🌟 Exercise 2: Dogs
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return f'{self.name} wins the fight'
        elif self_score < other_score:
            return f'{other_dog.name} wins the fight'
        else:
            return 'It\'s a tie!'


# Step 2: Create Dog Instances (3 dogs)
dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Max", 3, 25)
dog3 = Dog("Luna", 7, 18)

# Step 3: Test Dog Methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

## 🌟 Exercise 3: Dogs Domesticated
# pet_dog.py
import random
from exercice_3.dog import Dog  # Step 1 : import de la classe Dog

# Step 2 : PetDog hérite de Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)   # on réutilise __init__ de Dog
        self.trained = False                  # attribut spécifique à PetDog

    def train(self):
        print(self.bark())                    # affiche le bark hérité de Dog
        self.trained = True                   # le chien est maintenant entraîné

    def play(self, *args):
        # *args = liste d'instances PetDog qui jouent ensemble
        dog_names = ", ".join([dog.name for dog in args])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")


# Step 3 : Test
fido  = PetDog("Fido",  2, 10)
buddy = PetDog("Buddy", 3, 12)
max_  = PetDog("Max",   4, 15)

fido.train()              # entraîne Fido
fido.play(buddy, max_)    # Fido joue avec Buddy et Max
fido.do_a_trick()         # Fido fait un tour aléatoire

#  Exercise 4: Family and Person Classes
#Step 1: Create the Person Class
class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

        print(f"No person named {first_name} found in the family.")


    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")