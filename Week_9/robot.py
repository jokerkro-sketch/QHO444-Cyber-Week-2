# robot.py

class Robot:
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    @staticmethod
    def the_laws():
        print(Robot.laws)

    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")

    def __init__(self, name="Robot"):

        self.name = name
        self.age = 30
        self.energy = 20

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age} , energy={self.energy})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'

    def display(self):

        print(f"I am {self.name}")

if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(repr(robot))