import random

def main():
    max_num = 10

    min_num = 1

    guess = random.randint(min_num,max_num) # --- THis will get a number between  1 to 10 ---

    number=int(input(f" Enter your guess (Between { min_num } and  { max_num}): ")) # --- This for us to guess an number ---

    if number == guess:

        print (" you guessed the number")

    else:

        print (f" you guessed the wrong number,The number was {guess}")


main()
