

import random 

print("guess the number")

random_number = random.randint(1,10)
tries = 0
proceed = True

while proceed == True: 
    num = eval(input("Enter an intiger from 1 to 10: "))

    tries += 1

    if num == random_number: 
        print("You're guess is CORRECT! ")
        print(f"only took {tries} tries")
        break

    else:
        print("Wrong Guess")
        print("Continue guessing")
        continue
