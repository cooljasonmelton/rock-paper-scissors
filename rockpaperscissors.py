from random import randint
import time

#  get user input
print("rock...")
time.sleep(.5)
print("paper...")
time.sleep(.5)
print("scissors...")
time.sleep(.5)
print("shoot!")
time.sleep(.5)
user_input = input("Enter Choice: ").lower().strip()

# make sure getting correct option
correct_input = False
if  user_input == "rock" or user_input == "paper" or user_input == "scissors":
    correct_input = True
while correct_input == False:
    new_input = input("Please enter 'rock', 'paper' or 'scissors': ")
    if new_input == "rock" or new_input == "paper" or new_input == "scissors":
        user_input = new_input
        correct_input = True
    

# computer Choice
options = ["rock", "paper", "scissors"]
random_index = [randint(0,2)] 
computer_choice = options[random_index[0]]

# test user input against computer
result = "It's a tie!"
if user_input == "rock" and computer_choice == "scissors":
    result = "Rock blunts scissors! :-)"

if user_input == "rock" and computer_choice == "paper":
    result = "Paper covers rock. :-("

if user_input == "paper" and computer_choice == "rock":
    result = "Paper covers rock! :-)"

if user_input == "paper" and computer_choice == "scissors":
    result = "Scissors cuts paper. :-("

if user_input == "scissors" and computer_choice == "paper":
    result = "Scissors cuts paper! :-)"

if user_input == "scissors" and computer_choice == "rock":
    result = "Rock blunts scissors. :-("

# print results
print("You chose: ", user_input)
print("The computer chose: ", computer_choice)
print(result)




