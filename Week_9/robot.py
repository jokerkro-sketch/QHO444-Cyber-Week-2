# robot.py
# Definicja podstawowej klasy Robot

class Robot:
    # Atrybuty klasowe
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    @staticmethod
    def the_laws():
        """
        Metoda statyczna – nie wymaga instancji klasy.
        """
        print(Robot.laws)

    @classmethod
    def assemble(cls):
        """
        Metoda klasowa – tworzy i zwraca nowy obiekt klasy Robot.
        """
        return cls("Assembled Robot")

    def __init__(self, name="Robot"):
        """
        Konstruktor klasy Robot.
        """
        # Atrybuty instancji
        self.name = name
        self.age = 0
        self.energy = 0

    def display(self):
        """
        Metoda instancji wyświetlająca nazwę robota.
        """
        print(f"I am {self.name}")


# Kod testowy
if __name__ == "__main__":
    robot = Robot()
    robot.display()
