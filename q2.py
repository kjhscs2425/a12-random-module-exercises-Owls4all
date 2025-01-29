import random as r
# Make a random pet.

# Choose:
# Type of animal (at least 3 choices, string)
animal = r.choice(["bear","wolf","horse"])
# Age (integer)
if animal == 'bear':
    type = r.choice["polar","brown","black","grizzly"]
    if type == 'polar':
        age = str(r.randint(0,30))+"-year-old"
        weight = str(r.uniform(300,800))+" kilograms"
    if type == 'brown':
        age = str(r.randint(0,44))+"-year-old"
        weight = str(r.uniform(41,250))+" kilograms"
if animal == 'wolf':
    type = r.choice([])
    if type == '':
        pass
if animal == 'horse':
    type = r.choice([])

# Print a summary of your pet using an f-string
print(f"Your pet is a {age} {type} {animal}, weighing {weight}.")#REPLACE THIS WITH YOUR CODE