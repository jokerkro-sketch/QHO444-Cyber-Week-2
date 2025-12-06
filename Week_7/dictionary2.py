# Function from Activity 1: creates and returns a dictionary
def pattern():
    sequences = {
        "Short Sequence": 3,
        "Medium Sequence": 2,
        "Long Sequence": 1
    }
    return sequences


# Function to display only keys
def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()  # empty line for readability


# Function to display only values
def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()  # empty line for readability


# Function to display key-value pairs
def display_items(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()  # empty line for readability


# Function to run the program
def run():
    data = pattern()   # get the dictionary

    print("Dictionary:")
    print(data)
    print()

    display_keys(data)
    display_values(data)
    display_items(data)


# Run automatically
if __name__ == "__main__":
    run()