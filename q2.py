import random as r
# Make a random pet.
type=""
age=""
weight=""
# Choose:
# Type of animal (at least 3 choices, string)
animal = r.choice(["bear","wolf","horse"])
# Age (integer)
if animal == 'bear':
    type = r.choice(["polar","brown","black","grizzly"])
    if type == 'polar':
        age = str(r.randint(0,30))+"-year-old"
        weight = str(r.uniform(300,800))+" kilograms"
    if type == 'black':
        age = str(r.randint(0,44))+"-year-old"
        weight = str(r.uniform(41,250))+" kilograms"
    if type == 'brown':
        age = str(r.randint(0,47))+"-year-old"
        weight = str(r.uniform(80,600))+" kilograms"
    if type == 'grizzly':
        age = str(r.randint(0,44))+"-year-old"
        weight = str(r.uniform(95,389))+" kilograms"
if animal == 'wolf':
    type = r.choice(["silver","arctic","golden"])
    age = str(r.randint(0,13))+"-year-old"
    weight=str(r.uniform(12,79))+" kilograms"
if animal == 'horse':
    type = r.choice(["something"])

# Print a summary of your pet using an f-string
print(f"Your pet is a {age} {type} {animal}, weighing {weight}.")#REPLACE THIS WITH YOUR CODE