passwords = [
    {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
    ]

#Check whether all passwords are at least 8 characters long
#Version 1 using forloop
def are_all_passwords_long_enough(passwords):
    for password in passwords:
        if len(password['password']) < 8:
            return False
    return True

print(are_all_passwords_long_enough(passwords))


#version 2 using filter
def is_too_short(password):
    return len(password['password']) < 8

def are_all_passwords_long_enough(passwords):
    return len(list(filter(is_too_short,passwords))) == 0

print(are_all_passwords_long_enough(passwords))


#version 2.1 getting rid of if_too_short using lambda
def are_all_passwords_long_enough(passwords):
    return list(filter(lambda password: len(password['password']) < 8, passwords)) == []

print(are_all_passwords_long_enough(passwords))


#version 3 list comprehension
def are_all_passwords_long_enough(passwords):
    return len([password for password in passwords if len(password['password']) < 8]) == 0

print(are_all_passwords_long_enough(passwords))