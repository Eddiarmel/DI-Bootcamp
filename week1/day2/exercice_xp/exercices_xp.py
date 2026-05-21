
"""
🌟 Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

"""
#  the solution 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)


"""
Exercise 2: Cinemax #2
Key Python Topics:

Looping through dictionaries
Conditionals
Calculations
"""
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
money= 0
for key, value in family.items():
    if value < 3:
        print(f"{key} is free")
    elif 3 <= value < 12:
        print(f"{key} you have to pay for tickets 10 dollars")
        money += 10
    else:
        print(f"{key} you have to pay for tickets 15 dollars")
        money += 15

print(f"Total money collected: {money} $")

"""
Exercise 3: Zara
Key Python Topics:

Creating dictionaries
Accessing and modifying dictionary elements
Dictionary methods like .pop() and .update()

"""
rand={"name": "Zara",
      "creation_date": 1975,
      "creator_name": "Amancio Ortega Gaona",
      "type_of_clothes": ["men", "women", "children", "home"],
      "international_competitors": ["Gap", "H&M", "Benetton"],
      "number_stores": 7000,
      "major_colors": {
          "France": ["blue"],
          "Spain": ["red"],
          "US": ["pink", "green"]
      }}
## Change the value of number_stores to 2
rand["number_stores"] = 2
#Print a sentence describing Zara’s clients using the type_of_clothes key
print(f"Zara's clients are {', '.join(rand['type_of_clothes'])}.")
# Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in rand:
    rand["international_competitors"].append("Desigual")
#Delete the creation_date key
rand.pop("creation_date",None)
#Print the last item in international_competitors.
print(rand["international_competitors"][-1])
#Print the major colors in the US.
print(f"Major colors in the US: {', '.join(rand['major_colors']['US'])}.")
#Print the number of keys in the dictionary.
print(f"Number of keys in the dictionary: {len(rand)}")
#Print all keys of the dictionary.
print(f"Keys in the dictionary: {list(rand.keys())}")


"""
Exercise 4 : Some Geography
"""

#Step 1: Define a Function with Parameters
def describe_city(city,country="Inconnu"):
#Step 2: Print a Description
    print(f"{city} is in {country}.")
#Step 3: Call the Function
# describe_city()
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
    

"""
 Exercise 5 : Random
"""
# Step 1: Import the random Module
import random

def random_number():
    while True:
        number=input("Enter a number between 1 and 100")
        try:
          if  1 <= int(number) <= 100:
             number_int=int(number)
             break
          else:
            print("Number must be between 1 and 100. Please try again.")    
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    random_num = random.randint(1, 100)
    # Step 4: Compare the Numbers
    if number_int == random_num:
        print("Success! (if the numbers match)")
    else:
        print(f"Fail! Your number: {number_int}, Random number: {random_num} (if they don't match)")

#main program
random_number()


## Exercise 6 : Let’s create some personalized shirts !

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")


""" Exercise 7 : Temperature Advice """
#Create the get_random_temp() Function
def get_random_temps():
   temp=random.randint(-10,40)
   return temp

#Step 2: Create the main() Function
""" Exercise 7 : Temperature Advice """

import random

# Create the get_random_temp() Function
def get_random_temps():
    temp = random.randint(-10, 40)
    return temp

# Step 2: Create the main() Function
def main():
    temp = get_random_temps()

    print(f"The current temperature is {temp}°C.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")

    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")

    elif 16 <= temp < 23:
        print("The weather is nice. A light jacket should be fine.")

    elif 23 <= temp < 32:
        print("It's warm outside! Perfect for a t-shirt.")

    else:
        print("It's really hot! Stay hydrated and wear sunscreen.")

main()

"""
   🌟 Exercise 8: Pizza Toppings

"""
THE_BASE_PIZZA_PRICE = 10
topping_price = 0   
while True:
    print("Enter a pizza topping (or 'quit' to finish):")
    try:
     ingredients=input(" : ")
    except Exception as e:
        print(f"An error occurred: {e}")
    if ingredients == "quit":
        break
    print(f"Adding {ingredients} to the pizza.")
    topping_price += 2.5

print(f"Total price for the pizza: ${THE_BASE_PIZZA_PRICE + topping_price:.2f}")