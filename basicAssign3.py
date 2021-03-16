# Andrew Grant
#105226219

import random

num = random.randint(1, 9)

guess = int(input("Enter your guess (1-9): "))

if (guess == num):
    print("You Guessed It!!! :)")
else:
    print(f'Incorrect. The Number Was {num}.')