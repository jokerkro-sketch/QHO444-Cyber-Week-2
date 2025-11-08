def display_ladder(steps):
    for i in range(steps):
        print("| |")
        print("***")
    print("| |")

def create_ladder():
    steps = int(input("How many steps you need?\n"))
    display_ladder(steps)

create_ladder()