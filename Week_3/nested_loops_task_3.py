user = int(input("Please enter a sequence:")

marker = input("Please enter the character of a marker:")

is_counting = False
count = 0

for character in user:

if (is_counting == False) and (character == marker):
     print("we found first marker")
    is_counting = True
elif (is_counting == True) and (character == marker):
     print("We found 2nd marker")
    elif is_counting:
        count += 1

print(f"The distance between the markers is {count}.")