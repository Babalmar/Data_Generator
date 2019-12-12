import random
import json

name_surname = []
nick = ""
e_mail = ""
address = ""



def names():
    first_names = []
    last_names = []
    with open("person.txt", "r") as f:
        for line in f:
            person = line.split()
            first_names.append(person[0])
            last_names.append(person[1])
    name_surname.append(random.choice(first_names))
    name_surname.append(random.choice(last_names))
    return name_surname


def gen_nick():
    nick_list = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            nick_list.append(line)
    nick = nick_list[random.choice(nick_list)] + str(random.randint(1,100))
    return nick

def email():
    email_body = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            email_body.append(line)
    domain = [".com", ".org", ".mil", ".net", ".edu", ".pl", ".de", ".fr", ".ie", ".us", ".co.uk"]
    local_part = random.choice(email_body)
    host_name = random.choice(email_body)
    mail_domain = random.choice(domain)
    full_mail = local_part + "@" + host_name + mail_domain
    return full_mail


e_mail = email()


def generate_address():
    code = []
    street = []
    city = []
    with open("address.txt", "r") as f:
        for line in f:
            address_data = line.split(",")
            code.append(address_data[0])
            street.append(address_data[1])
            city.append(address_data[2])
    city_code = random.choice(code)
    city_name = random.choice(city)
    city_street = random.choice(street)
    full_address = city_code + " " + city_name.strip('\n') + ", " + city_street + " " + str(random.randint(1, 100))
    return full_address


address = generate_address()


def save_to_json():
    data_to_json = {"First name:": name_surname[0], "Last name:": name_surname[1], "Nick:": nick, "E-mail:": e_mail,
                    "Address:": address}

    json_string = json.dumps(data_to_json)
    with open("data.json", "w") as f:
        f.write(json_string)


def save_to_xml(fileName):
    import xml.etree.ElementTree as xml

    root = xml.Element("Test data")
    cl = xml.Element("User")
    root.append(cl)
    address1 = xml.SubElement(cl, "Address")
    address1.text = address

    email1 = xml.SubElement(cl, "Email")
    email1.text = e_mail

    tree = xml.ElementTree(root)
    with open(fileName, "wb") as files:
        tree.write(files)


names()
save_to_json()
save_to_xml("User.xml")