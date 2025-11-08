# built_in_functions.py

print("Program Started!")
character = input("Please enter ONLY 1 character!: ")

if len(character) == 1:
    # ord zwraca kod punktu Unicode dla znaku; dla standardowego ASCII wartości to 0-127
    print(f"The ASCII code for {character} is {ord(character)}.")
else:
    print("Error WRONG NUMBER OF CHARACTERS!!!: Please enter exactly one character.")

print("Program Ended!")