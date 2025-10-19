# Enter your name
#print("What is your name: ")
name = input("What is your name: ")

# Enter your age
print("What is your Age: ")
age = int(input())

# Enter your weight
print("What is your weight: ")
weight = float(input())

# Enter your height
print("What is your height: ")
height = float(input())

bmi = weight / (height ** 2)

print(f"Hi {name} and your bmi {bmi}")