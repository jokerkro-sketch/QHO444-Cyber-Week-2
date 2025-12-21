from Planet import planet
from Robot import Robot
from Human import Human

class Universe:

    def __init__(self):
        self.planet = []

    def __repr__(self):
        return f"universe (planet: {self.planet})"

    def __str__(self):
        return f"The universe contains {len(self.planets)} planets"

    def generate(self):
        for i in range(random.randint(1,10)):
            human = Human(f"Human{index}")
            planet.add_human(human)

        for index in range(random.randint(1,10)):
            robot = Robot(f"Robot{index}")
            planet.add_robot(robot)

        self.planets.append(planet)

    def show_pop(self, selection):

        x_values = []
        y_values = []

        for planet in self.planets:
            x_values.append(planet.name)

            if selection == "humans":
                y_values.append(len(planet.inhabitants['humans']))
            else:
                