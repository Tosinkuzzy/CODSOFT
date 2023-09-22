#!/usr/bin/python3

import random
import string

def generate_password():
    pwd_length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity of the password (low/medium/high): ")

    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + "!" + "\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    password = "".join(random.choice(characters) for _ in range(pwd_length))
    print("Generated Password:", password)

generate_password()

