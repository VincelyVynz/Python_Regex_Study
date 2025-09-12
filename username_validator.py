import re

#Username Validation (only lowercase letters with a length of 3-5)
username = input("Enter your name: ")

if re.fullmatch(r"[a-z][\w]{2,4}", username):
    print("Your name is valid")
else:
    print("Your name is not valid")

