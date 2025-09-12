#Todo Username Validation (only lowercase letters with a length of 3-5)

import re

username = input("Enter your name: ")

if re.fullmatch(r"[a-z]{3,5}", username):
    print("Your name is valid")
else:
    print("Your name is not valid")