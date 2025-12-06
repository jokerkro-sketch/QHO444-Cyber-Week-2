
file = open('sample.txt', 'w') as file:
    file.write('to co pisze sie teraz wyswietli')


file = open('sample.txt', 'r') as file:
    content = file.read()
    print(content)