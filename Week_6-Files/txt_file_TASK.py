import os

def cwd():
    path = os.getcwd()
    print(f"Current working directory is {path}")
    print(f"Current directory contain the following files:")

    for file in os.listdir(path):
        print(file)

cwd()

def abc():

    path = os.getabc()
    print(f"witamy wiesniaki {path}")
    print(f"zobaczymy sie niebawem {path}")

    for file in os.listdir(path):
        print(file)



cwd()