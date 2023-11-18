import string
import secrets

def upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def symbol(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(lenght,symbol,uppercase):
    combination = string.ascii_lowercase + string.digits

    if symbol:
        combination += string.punctuation

    if uppercase:
        combination = string.ascii_uppercase

    combination_length = len(combination)
    new_password = ''

    for i in range(lenght):
        new_password += combination[secrets.randbelow(combination_length)]
    return new_password

for i in range(1,6):
    password = generate_password(lenght=10,symbol=True,uppercase=False)
    space = f'U: {upper(password)}, S: {symbol(password)} '
    print(f'{i} --> {password} ({space})')