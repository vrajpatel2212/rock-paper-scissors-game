import random
name = input("Enter your name:")
print("Welcome", name , "\nLet's play a game!")
print("Game's name is : Rock, Paper, Scissors")
user_input = input("Enter your choice:")
print("You chose:", user_input)
computer_choice = random.choice(["rock", "paper", "scissors"])
print("Computer chose :", computer_choice)
if user_input == "rock" and computer_choice == "scissors":
  print("YOU WIN!!")
elif user_input == "paper" and computer_choice == "rock":
  print("YOU WIN!!")
elif user_input == "scissors" and computer_choice == "paper":
  print("YOU WIN!!")
elif user_input == "scissors" and computer_choice == "rock":
  print("YOU LOSE!!")
elif user_input == "rock" and computer_choice == "paper":
  print("YOU LOSE!!")
elif user_input == "paper" and computer_choice == "scissors":
  print("YOU LOSE!!")
else:
  print("It's a draw")
user_input = input("DO you wamt to play again (yes/no):")
if user_input == "yes":
  while user_input == "yes":
    print("Welcome", name , "\nLet's play a game!")
    user_input = input("Enter your choice:")
    print("You chose:", user_input)
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose :", computer_choice)
    if user_input == "rock" and computer_choice == "scissors":
      print("YOU WIN!!")
    elif user_input == "paper" and computer_choice == "rock":
      print("YOU WIN!!")
    elif user_input == "scissors" and computer_choice == "paper":
      print("YOU WIN!!")
    elif user_input == "scissors" and computer_choice == "rock":
      print("YOU LOSE!!")
    elif user_input == "rock" and computer_choice == "paper":
      print("YOU LOSE!!")
    elif user_input == "paper" and computer_choice == "scissors":
      print("YOU LOSE!!")
    else:
      print("It's a draw")
      break
  else:
    print("It was fun playing with you", name,"\nThank you for playing \nSee you soon!")
  
