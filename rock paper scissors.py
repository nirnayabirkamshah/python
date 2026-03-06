import random

import  random

rock = "rock"
paper = "paper"
scissors = "scissors"
beats = {
    rock: scissors ,
    paper:rock ,
    scissors:paper ,
}
name = input("Enter your name :")
user = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice([rock,paper,scissors])
print(f"The computer chose {computer}")
if user == computer:
    print("It's a draw")
elif beats[user] == computer:
    print(f"The computer chose {computer}, computer won")
else:
    print(f"{name} won")
