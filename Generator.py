import random

first_names = []
last_names = []
sex = ["Male", "Female", "Unknown"]

def names():
    with open("person.txt", "r") as f:
        for line in f:
            person = line.split()
            first_names.append(person[0])
            last_names.append(person[1])

def email():
    email_body = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            email_body.append(line)
    domain = [".com", ".org", ".mil", ".net", ".edu", ".pl", ".de", ".fr", ".ie", ".us", ".co.uk"]
    local_part = email_body[random.randint(0, len(email_body)-1)]
    host_name = email_body[random.randint(0, len(email_body)-1)]
    mail_domain = (domain[random.randint(0, len(domain)-1)])
    full_email = local_part + "@" + host_name + mail_domain
    return full_email

random_mail = email()

def generate_data(random_mail):
    print("First name: {}".format(first_names[random.randint(0, len(first_names) - 1)]))
    print("Last name: {}".format(last_names[random.randint(0, len(last_names) - 1)]))
    print("Sex: {}".format(sex[random.randint(0, len(sex) - 1)]))
    print("E-mail: {}".format(random_mail))

def save_to_file():
    pass

names()
generate_data(random_mail)