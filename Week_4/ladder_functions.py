def display_ladder(steps):
    for steps in range(steps):
        print("| |")
        print("***")
    print("| |")

def create_ladder():
    steps = int(input("How many steps you need?\n"))
    display_ladder(steps)

def second_ledder():
    steps2 = int(input("How many steps you need on 2cond one?\n"))
    display_ladder(steps2)

create_ladder()
second_ledder()