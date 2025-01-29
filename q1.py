import random as r
def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  #YOUR CODE HERE
  color = r.choice(['red','green','yellow','blue'])
  side = r.choice(['left','right'])
  appendage=r.choice(['hand','foot'])
  return f'Put your {side} {appendage} on {color}.'

# Here's the function call. This should print a random assortment of twister commands
for i in range(10):
  print(spin_twister_spinner())