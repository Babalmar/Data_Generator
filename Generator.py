import random


def main():
    menu = """
    Select F for first name
    Select L for last name
    Select N for nick
    Select E for e-mail
    Select A for address
    Select S for full set 
    Select J for JSON
    Select X for XML 
    Select Q to quit
    
    Select: 
    """

    selection = input(menu)

    while selection not in ("Q", "q"):
        if selection in ("F", "f"):
            name_surname = names()
            print("First name: {}".format(name_surname[0]))
        elif selection in ("L", "l"):
            name_surname = names()
            print("Last name: {}".format(name_surname[1]))
        elif selection in ("N", "n"):
            nick = gen_nick()
            print("Nick: {}".format(nick))
        elif selection in ("E", "e"):
            e_mail = email()
            print("E-mail: {}".format(e_mail))
        elif selection in ("A", "a"):
            address = generate_address()
            print("Address: {}".format(address))
        elif selection in ("S", "s"):
            name_surname = names()
            nick = gen_nick()
            e_mail = email()
            address = generate_address()
            full_set(name_surname, nick, e_mail, address)
        elif selection in ("J", "j"):
            name_surname = names()
            nick = gen_nick()
            e_mail = email()
            address = generate_address()
            save_to_json(name_surname, nick, e_mail, address)
        elif selection in ("X", "x"):
            name_surname = names()
            nick = gen_nick()
            e_mail = email()
            address = generate_address()
            save_to_xml(name_surname, nick, e_mail, address)
        else:
            print("Unknown command")
        input("Press any to continue...")
        selection = input(menu)
    print("Program terminated")


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


def gen_nick():
    nick_list = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            nick_list.append(line)
    nickname = random.choice(nick_list) + str(random.randint(1, 100))
    return nickname.capitalize()


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


def full_set(name_surname, nick, e_mail, address):

    data = {"First name": name_surname[0], "Last name": name_surname[1],
            "Nick": nick, "E-mail": e_mail, "Address": address}

    for key, value in data.items():
        print(key + ":" + value)
    return data


def save_to_json(name_surname, nick, e_mail, address):
    import json

    json_data = {"First name": name_surname[0], "Last name": name_surname[1], "Nick": nick, "E-mail": e_mail,
                 "Address": address}

    json_string = json.dumps(json_data)

    with open("data.json", "w") as f:
        f.write(json_string)

    print(json_string)
    print("Test data saved to data.json file")


def save_to_xml(name_surname, nick, e_mail, address):
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

    print("Test data saved to user.xml file")


main()
