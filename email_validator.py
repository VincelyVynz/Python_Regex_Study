import re

#  Email Validation
#  Username: at least 3 characters, letters/digits/underscore/dot allowed
#  Domain: at least 2 lowercase letters
#  Extension: 2–3 lowercase letters

email = input("Enter your email: ").strip()

if re.fullmatch(r"[\w\.]{3,}@[a-z]{2,}\.[a-z]{2,3}", email):
    print("Your email is valid")
else:
    print("Your email is not valid")