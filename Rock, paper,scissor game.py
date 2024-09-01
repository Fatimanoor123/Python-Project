import random

user_wins=0
computer_win=0
options=["rock", "paper", "scissor"]
while True:
  user_input=input("Rock/Paper/Scissors/ Q for quit: ").lower()
  if user_input=="q":
    break
  if user_input not in options:
    continue
  random_number=random.randint(0,2)
  computer_pick=options[random_number]
  print("Computer picked", computer_pick + ".")
  
  if user_input=="rock" and computer_pick=="scissors":
    print("You won!")
    user_wins +=1 
  elif user_input=="paper" and computer_pick=="rock":
    print("You won!")
    user_wins +=1
  elif user_input=="scissors" and computer_pick=="paper":
    print("You won!")
    user_wins +=1
  else:
    print("You lost!")
    computer_win +=1
  
print("You won", user_wins, "times.")
print("Computer wins", computer_win, "times")
print("Goodbye!")
