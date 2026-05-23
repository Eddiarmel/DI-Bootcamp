# dog.py
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} says Woof!'

    def __str__(self):
        return f'{self.name}, age {self.age}, weight {self.weight}kg'