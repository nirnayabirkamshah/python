import  random
guess = random.randint(1,10)
tries =0
# --- Now the user will guess ---
while True:
 user_guess =int(input("Guess a number between 1 to 10: "))
 tries =tries  +1
 if user_guess == guess:
    print(f"You are right ,you guessed it with in {tries} tries , 🎉🎉 ")
 elif user_guess >= guess :
    print("To High it was , Try again ")
 elif user_guess == str('end'):
     break
 else:
    print("To Low it was ,  Try again")
