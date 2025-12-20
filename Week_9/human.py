# human.py

class Human:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 38
        self.energy = Human.MAX_ENERGY

    def __repr__(self):
        return f'Human(name={self.name}, age={self.age} , energy={self.energy})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

    def display(self):
        print(f"I am {self.name}")

if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
