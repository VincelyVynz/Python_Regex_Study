import re

#  Email Validation
#  Username: at least 3 characters, letters/digits/underscore/dot allowed
#  Domain: at least 2 lowercase letters
#  Extension: 2–3 lowercase letters

def validate_email(email):
    ext_list = ["com", "in", "edu", "net", "io", "org", "co"]
    at_count = 0
    dot_count = 0
    error_list = []
    for char in email:
        if char == "@":
            at_count += 1
    if at_count == 0:
        error_list.append("Email does not contain @, must contain one @ character.")
    elif at_count > 1:
        error_list.append("Email contains more than one @ character, must contain only one @ character.")

    else:
        username, domain_ext = email.split("@")

        for char in domain_ext:
            if char == ".":
                dot_count += 1
        if dot_count == 0:
            error_list.append("Email does not contain ., must contain one '.' character.")
        elif dot_count > 1:
            error_list.append("Email contains more than one '.' character, must contain only one '.' character.")
        else:
            domain, ext = domain_ext.split(".")
            if not re.fullmatch(r"^[a-z][\w.-]{1,18}[a-z0-9]$", username):
                error_list.append("Username must start with a lowercase letter, end with a lowercase letter or a number, can have underscores or hyphen.")

            if not re.fullmatch(r"[a-z]{2,10}", domain):
                error_list.append("Domain must contain 3 to 10 lowercase letters.")

            if ext not in ext_list:
                error_list.append("Invalid domain extension.")


    if error_list:
        return f"{email} is invalid.\n" + "\n".join(f"{error}" for error in error_list)
    else:
        return f"{email} is valid."



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

#Old validation

# if re.fullmatch(r"[\w\.]{3,}@[a-z]{2,}\.[a-z]{2,3}", email):
#     return f"{email} is valid."
# else:
#     return f"{email} is not valid."