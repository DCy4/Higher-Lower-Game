""" 
Higher Lower Game 
David C
02/01/23
"""
from art import logo, vs
from game_data import data
import random
import clear


"""takes an int to either 1: print compare or 2: print against. takes a dictionary index and returns print(f"Compare B: {name}, a {description}, from {country}.) """
def print_entry(num, dict_entry):
  instance = ""
  letter = ""
  if num == 1:
    instance = "Compare"
    letter = "A"
  else:
    instance = "Against"
    letter = "B"
    
  name = dict_entry["name"]
  description = dict_entry["description"]
  country = dict_entry["country"]
  
  print(f"{instance} {letter}: {name}, a {description}, from {country}.")

"""Takes follower count int and returns str"""
def compare(A, B):
  if A > B:
    return "A"
  else:
    return "B"

def print_score():
  global score
  if score > 0:
    print(f"You're right. Current score: {score}")
  else:
    return
    
def game():
  global score
  global game_end
  while not game_end:  
    print(logo)
    print_score()
    #select random entry from dictionary
    entry_a = data[random.randrange(len(data))]
    #select second random entry from dictionary
    entry_b = data[random.randrange(len(data))]
    #check for duplicates 
    while entry_a == entry_b:
      entry_b = data[random.randrange(len(data))]
    
    print_entry(1,entry_a)
    #print vs image
    print(vs)
    print_entry(2,entry_b)
    
    #compare follower count
    fol_a = entry_a["follower_count"]
    fol_b  = entry_b["follower_count"]
    answer = ""
    if fol_a > fol_b:
      answer = "A"
    else: 
      answer = "B"
    #ask user for answer
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    #compare user answer
    if user_answer.lower() == answer.lower():
      score += 1
      #clear screen
      return clear()
    else:
      game_end = True
      clear()
      print(f"Sorry that's wrong. Final score: {score}")

#flag 
game_end = False
score = 0
#show logo
game()


