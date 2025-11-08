# program weryfikacji szlachectwa

def name():
    name = input('Enter your name: ')
    print("Hello " + name)
    return name  # zwraca imię, żeby można było użyć dalej

def surname():
    surname = input('Enter your surname: ')
    print('Mr., ' + name + surname )
    return surname  # zwraca nazwisko

def verification(name, surname):
    answer = input('Are you a Prince? (yes/no): ').lower()
    if answer == "yes":
        print(f'Hello Prince {name} {surname} wiedzialem że jesteś błękitnej krwi! Takie rzeczy widać odrazu Książe!!!')
    else:
        print(f'Goń sie, {name} {surname}.')


name = name()
surname = surname()
verification(name, surname)