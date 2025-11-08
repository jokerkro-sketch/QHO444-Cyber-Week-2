print("Program started...")

user = input("Please enter standard character")

if len(user) == 1:
    print(f"The ASCII code for {user} is {ord(user)}")
else:
    print("A single character was expected...")

print("Program ended!")
