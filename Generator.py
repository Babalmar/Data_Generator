import random


def main():
    menu = """
    Select F for first name
    Select S for surname
    Select N for nick
    Select E for e-mail
    Select A for address
    Select G for full set (with json & xml)
    Select Q to quit\n
    """
    selection = input(menu)

    if selection in ("F", "f"):
        print("First name: {}".format(name_surname[0]))
    elif selection in ("S", "s"):
        print("Last name: {}".format(name_surname[1]))
    elif selection in ("N", "n"):
        print("Nick: {}".format(nick))
    elif selection in ("E", "e"):
        print("E-mail: {}".format(e_mail))
    elif selection in ("A", "a"):
        print("Address: {}".format(address))
    elif selection in ("G", "g"):
        for key, value in test_data.items():
            print(key, value)
        save_to_xml()
    elif selection in ("Q", "q"):
        print("Program terminated")
    else:
        print("Unknown command")


def names():
    name_and_surname = []
    first_names = []
    last_names = []
    with open("person.txt", "r") as f:
        for line in f:
            person = line.split()
            first_names.append(person[0])
            last_names.append(person[1])
    name_and_surname.append(random.choice(first_names))
    name_and_surname.append(random.choice(last_names))
    return name_and_surname


name_surname = names()


def gen_nick():
    nick_list = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            nick_list.append(line)
    nickname = random.choice(nick_list) + str(random.randint(1, 100))
    return nickname


nick = gen_nick()


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
    address = city_code + " " + city_name.strip('\n') + ", " + city_street + " " + str(random.randint(1, 100))
    return address


address = generate_address()


def save_to_json():
    import json

    data_to_json = {"First name:": name_surname[0], "Last name:": name_surname[1], "Nick:": nick, "E-mail:": e_mail,
                    "Address:": address}

    json_string = json.dumps(data_to_json)
    with open("data.json", "w") as f:
        f.write(json_string)

    return data_to_json

test_data = save_to_json()

def save_to_xml():
    import xml.etree.ElementTree as xml

    root = xml.Element("Test data")
    cl = xml.Element("User")
    root.append(cl)

    name1 = xml.SubElement(cl, "First name")
    name1.text = name_surname[0]

    surname1 = xml.SubElement(cl, "Last name")
    surname1.text = name_surname[1]

    nick1 = xml.SubElement(cl, "Nick")
    nick1.text = nick

    email1 = xml.SubElement(cl, "Email")
    email1.text = e_mail

    address1 = xml.SubElement(cl, "Address")
    address1.text = address

    tree = xml.ElementTree(root)

    with open("User.xml", "wb") as files:
        tree.write(files)

main()