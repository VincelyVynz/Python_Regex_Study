import re

#  Email Validation
#  Username: at least 3 characters, letters/digits/underscore/dot allowed
#  Domain: at least 2 lowercase letters
#  Extension: 2–3 lowercase letters

def validate_email(email):

    if re.fullmatch(r"[\w\.]{3,}@[a-z]{2,}\.[a-z]{2,3}", email):
        return f"{email} is valid."
    else:
        return f"{email} is not valid."

# Testing
if __name__ == "__main__":
    print(validate_email("alice99@mail.com"))     # valid
    print(validate_email("john.doe@abc.org"))     # valid
    print(validate_email("cat@me.io"))            # valid
    print(validate_email("a_b_c@mail.co"))        # valid

    print(validate_email("al@mail.com"))          # invalid (username < 3 chars)
    print(validate_email("alice@Mail.com"))       # invalid (capital M in domain)
    print(validate_email("carol@mail.c"))         # invalid (extension < 2)
    print(validate_email("bob@mail.comm"))        # invalid (extension > 3)
    print(validate_email("bobmail.com"))          # invalid (missing @)
    print(validate_email("dora@mailcom"))         # invalid (missing dot)
    print(validate_email("alex@ma_il.com"))       # invalid (underscore not allowed in domain)