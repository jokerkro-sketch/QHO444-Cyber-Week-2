with open("data.csv", "w", encoding="utf-8") as plik:
    plik.write("Imię,Nazwisko,Wiek\n")
    plik.write("Dominik,Kowalski,28\n")
    plik.write("Anna,Nowak,34\n")

print("Plik CSV został utworzony!")

