rows = int(input("How many rows should I have? "))

columns = int(input("How many columns should I have? "))

#Display grid

for row in range(0 , rows , 1):
    for column in range(0 , columns , 1):
        print(":-)", end="")

    print("end of loops....")

print("task comleted!!!")