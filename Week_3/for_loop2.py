steps_to_target = int(input("How far are we from the target? "))

for steps_remaining in range(steps_to_target,0,-1):
    print(steps_remaining, "steps remaining")

print("\n Target achieved!")
