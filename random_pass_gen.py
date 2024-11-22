import string
import os
import random

def generate_password(length):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    password = ''.join([random.choice(s) for _ in range(length)])
    return password

if __name__ == "__main__":
    plen = int(input("Enter the length of the password: "))
    password = generate_password(plen)
    print("Generated Password: ", password)
