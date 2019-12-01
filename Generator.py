import random

first_names = []
last_names = []
sex = ["Male", "Female", "Unknown"]

def names():
    with open("person.txt", "r") as f:
        for line in f:
            x = line.split()
            y = x[0]
            z = x[1]
            first_names.append(y)
            last_names.append(z)

def e_mail():
    pass

def generate_data():
    print("First name: {}".format(first_names[random.randint(0, len(first_names) - 1)]))
    print("Last name: {}".format(last_names[random.randint(0, len(last_names) - 1)]))
    print("Sex: {}".format(sex[random.randint(0, len(sex) - 1)]))

names()
generate_data()