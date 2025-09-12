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