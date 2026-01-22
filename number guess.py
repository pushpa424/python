import random
num = random.randint(1, 50)
guess = int(input(" Guess a number between 1 and 50: "))
if guess == num:
    print("Correct")
else:
    print("wrong", num)
