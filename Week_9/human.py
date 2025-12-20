# human.py
# Definicja podstawowej klasy Human

class Human:
    # Atrybut klasowy (stała wspólna dla wszystkich obiektów)
    MAX_ENERGY = 100

    def __init__(self):
        """
        Konstruktor klasy Human.
        Ustawia wartości początkowe dla nowego obiektu.
        """
        # Atrybuty instancji
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        """
        Metoda instancji wyświetlająca nazwę obiektu.
        """
        print(f"I am {self.name}")


# Kod testowy – wykona się tylko, gdy plik uruchomimy bezpośrednio
if __name__ == "__main__":
    human = Human()
    human.display()