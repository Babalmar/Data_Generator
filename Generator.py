import random
import json

first_names = []
last_names = []
sex = ["Male", "Female", "Unknown"]
Data_To_File = []
Data_To_Json = {}

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
    first_name = first_names[random.randint(0, len(first_names) - 1)]
    print("First name: {}".format(first_name))
    Data_To_Json["First name:"] = first_name
    Data_To_File.append(first_name)
    last_name = last_names[random.randint(0, len(last_names) - 1)]
    print("Last name: {}".format(last_name))
    Data_To_Json["Last name:"] = last_name
    Data_To_File.append(last_name)
    Sex = sex[random.randint(0, len(sex) - 1)]
    print("Sex: {}".format(Sex))
    Data_To_Json["Sex:"] = Sex
    Data_To_File.append(Sex)
    print("E-mail: {}".format(random_mail))
    Data_To_Json["E-mail:"] = random_mail
    Data_To_File.append(random_mail)

def save_to_file():
    data_output = Data_To_File[0] + "," + Data_To_File[1] + "," + Data_To_File[2] + "," + Data_To_File[3]
    with open("test_data.txt", "w") as f:
        f.write(data_output)

def save_to_json():
    json_string = json.dumps(Data_To_Json)
    with open("data.json", "w") as f:
        f.write(json_string)

names()
generate_data(random_mail)
save_to_file()
save_to_json()