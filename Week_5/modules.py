import random

min_value = int(input("Enter a minimum value: "))

max_value = int(input("Enter a maximum value: "))

random_number = random.randrange(min_value, max_value)

print(f"""I am thinking of a number between 
    {min_value} and {max_value}.
    Can you guess what it is?""")

print("Can you guess the number?")

guess_correctly = False

while not guess_correctly:
    guess = int(input("Please enter a number: "))

    if guess == random_number:
        print("Good job, you guessed it!")
        guess_correctly = True
    elif guess > random_number:
        print("Guess number is too high")
    else:
        print("Guess number is lower")
