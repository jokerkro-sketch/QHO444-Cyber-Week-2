def observed_items():
    observations = []

    for i in range(7):
        item = input("Please enter an observation:\n")
        observations.append(item)

    return observations

def run_task2():
    print("Counting observations...")

    data = observed_items()

    result_set = set()

    for value in data:
        count_tuple = (value, data.count(value))
        result_set.add(count_tuple)

    print()
    for item, count in result_set:
        print(f"{item} observed {count} times.")


if __name__ == "__main__":
    run_task2()
