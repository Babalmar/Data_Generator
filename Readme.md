### Generator.py
Simple stand-alone terminal app that allows to generate random data: 
> First name 
> Last name 
> Nick 
> E-mail 
> Address
> Full set (display only)
> Full set (JSON)
> Full set (XML)

### Data_Generator_library.py

Data Generator library allows to generate a numer of random data:

    First name
    Last name
    E-mail
    Nick
    Address (Postal code, City, Street)
    Full set (including all of the above data)

Address and full set return data in the form of a dictionary, therefore a specific

Each of the the "generate" functions uses "ptf" input parameter - the default setting is "True".

if ptf is True:
  print("Generated data is saved into json file")
else:
  print("Json file is not updated")

Installation

Just copy Data_generator_library.py to your project folder.
Usage

import Data_generator_library as dg

newname = dg.generate_name(ptf=False)
print(newname)
# returns Wiesława 

newsurname = dg.generate_surname(ptf=False)
print(newsurname)
# returns Nowicka

newnick = dg.generate_nick(ptf=True)
print(newnick)
# returns Margherita12

newaddres = dg.generate_address(ptf=True)
print(newaddres)
# returns {'Postal code': '82-309', 'City': 'Warszawa', 'Street': 'ul. Gajowa 55'}

newmail = dg.generate_email(ptf=False)
print(newmail)
# returns private@clap.com

newset = dg.generate_full_set(ptf=False)
print(newset)
# returns {'First name': 'Jacek', 'Last name': 'Kozłowska', 'Nick': 'Elenor62', 'E-mail': 'punch@baby.com', 
'Address': {'Postal code': '00-159', 'City': 'Sopot', 'Street': 'ul. Nalewki 45'}}




