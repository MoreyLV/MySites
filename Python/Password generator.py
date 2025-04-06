import string
import random

digits = ''
lowercase = ''
uppercase = ''
punctuation = ''


def info(digits, lowercase, uppercase, punctuation):
    print("Choose options for the password:")

    if digits == '':
        print("1. Turn on numbers")
    else:
        print("1. Turn off numbers")
    if lowercase == '':
        print("2. Turn on lowercase")
    else:
        print("2. Turn off lowercase")
    if uppercase == '':
        print("3. Turn on uppercase")
    else:
        print("3. Turn off uppercase")
    if punctuation == '':
        print("4. Turn on punctuation")
    else:
        print("4. Turn off punctuation")
    print("5. Generate")
    onoff = int(input("Choose an option: "))
    if onoff == 1:
        if digits == '':
            digits = string.digits
        else:
            digits = ''
    elif onoff == 2:
        if lowercase == '':
            lowercase = string.ascii_lowercase
        else:
            lowercase = ''
    elif onoff == 3:
        if uppercase == '':
            uppercase = string.ascii_uppercase
        else:
            uppercase = ''
    elif onoff == 4:
        if punctuation == '':
            punctuation = string.punctuation
        else:
            punctuation = ''
    elif onoff == 5:
        generate_password(digits, lowercase, uppercase, punctuation)
        return
    info(digits, lowercase, uppercase, punctuation)

def generate_password(digits, lowercase, uppercase, punctuation):
    characters = digits + lowercase + uppercase + punctuation
    if not characters:
        print("No characters selected for the password.")
        return
    password = ''.join(random.choices(characters, k=12))
    print("Generated password:", password)

info(digits, lowercase, uppercase, punctuation)
