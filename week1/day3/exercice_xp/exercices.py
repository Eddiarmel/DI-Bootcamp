"""_🌟 Exercise 1: Cats
"""
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

##Step 1: Create cat objects
cat1 = Cat("Fluffy", 3)
cat2 = Cat("Whiskers", 5)
cat3 = Cat("Mittens", 2)
# Step 2: Create a function to find the oldest cat
def find_oldest_cat(c1,c2,c3):
    oldest_cat = c1
    if c2.age > oldest_cat.age:
        oldest_cat = c2
    if c3.age > oldest_cat.age:
        oldest_cat = c3
    return oldest_cat

# Step 3: Call the function and print the result
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


"""
_🌟 Exercise 2: Dogs
"""
# Step 1: Create the Dog Class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    # Create a bark() method that prints “<dog_name> goes woof!”
    def bark(self):
        print(f"{self.name} goes woof!")
    # Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
    
# Step 2: Create dog objects
# Create davids_dog and sarahs_dog objects with their respective names and heights
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 30)
#Step 3: Print Dog Details and Call Methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

#Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")


"_🌟 Exercise 3: Who’s The Song Producer?"
# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    # Create a sing_me_a_song() method that prints each element of lyrics on its own line.
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# Step 2: Create a Song Object
# Create a song object with the lyrics of your favorite song    my_favorite_song = Song(["Line 1 of the song", "Line 2 of the song", "Line 3 of the song"])
my_favorite_song = Song(["Yesterday, all my troubles seemed so far away",   "Now it looks as though they're here to stay",   "Oh, I believe in yesterday"])
my_favorite_song.sing_me_a_song() 

"🌟 Exercise 4: Afternoon At The Zoo"
# Step 1: Create the Zoo Class
class Zoo:
    # Implement the __init__() method
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    # Create an add_animal() method that adds a new animal to the animals list, if it isn’t already in the list.
    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
    # Create a get_animals() method that prints all the animals in the zoo.
    def get_animals(self):
        for animal in self.animals:
            print(animal)
    # Create a sell_animal() method that removes the animal from the list of animals, if it exists.
    def sell_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
    # Create a sort_animals() method that sorts the animals alphabetically and groups them based on their first letter.
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        return sorted_animals
    
def get_groups(self):
    groups = self.sort_animals()
    for letter, animals in groups.items():
        print(f"{letter}: {animals}")

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.get_groups()