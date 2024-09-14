"""
Write a program that asks users for their sandwich preferences. 
The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
"""

import pyinputplus as pyip

breads = {"wheat": 2,
          "white": 3,
          "sourdough": 4
          }

proteins = {"chicken": 10,
          "turkey": 7,
          "ham": 12,
          "tofu": 3
          }

cheeses = {"cheddar": 2,
          "swiss": 4,
          "mozzarella": 3
          }

extras = {"mayo": 1,
          "mustard": 1,
          "lettuce": 1,
          "tomato": 1
          }

# dictionary that merges every other dictionary. useful for checking the final price later on
full_sandwich_prices = breads | proteins | cheeses | extras

# will include every item in the sandwich
full_sandwich = []

print("What sandwich do you want?\n")
bread = pyip.inputMenu([bread_type for bread_type in breads.keys()], numbered=True, prompt="Pick a bread\n")
full_sandwich.append(bread)
print()

protein = pyip.inputMenu([protein for protein in proteins.keys()], numbered=True, prompt="Pick a protein\n")
full_sandwich.append(protein)
print()

if pyip.inputYesNo(prompt="Do you want cheese?\n") == "yes":
    cheese = pyip.inputMenu([cheese for cheese in cheeses.keys()], numbered=True, prompt="Pick a cheese then\n")
    full_sandwich.append(cheese)
else:
    cheese = ""
print()

chosen_extras = []
for extra in extras.keys():
    if pyip.inputYesNo(prompt=f"Do you want {extra}?\n") == "yes":
        chosen_extras.append(extra)
    print()
full_sandwich.extend(chosen_extras)

print(f"Your final sandwich is {bread}, {protein}, {cheese if cheese else 'no cheese'}, {', '.join(chosen_extras)}")


price = sum(full_sandwich_prices[item] for item in full_sandwich)
amount_of_sandwiches = pyip.inputInt(prompt="How many do you want?\n", min=1)
price *= amount_of_sandwiches

print(f"The total price is {price}")


# price is displayed at the end only. pitfall



