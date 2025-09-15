import re
#Jira Ticket Validator

# Validation conditions (Format: PROJECT-123)
# Project part = 2–5 uppercase letters
# Dash (-)
# Number part = 1-4 digits

def validate_jira_ticket(ticket):
    hyphen_count = 0
    error_list = []
    for char in ticket:
        if char == "-":
            hyphen_count += 1
    if hyphen_count == 0:
        error_list.append("Must contain one - character.")
    elif hyphen_count > 1:
        error_list.append("Must not contain more than one - character.")
    else:
        project, issue = ticket.split("-", 1)

        if not re.fullmatch(r"[A-Z]{2,5}", project):
            error_list.append("Jira project name must be 2 -5 uppercase letters.")

        if not re.fullmatch(r"[0-9]{1,4}", issue):
            error_list.append("Jira issue name must be 1 - 4 digits.")


    if error_list:
        return f"{ticket}\n" + "\n".join(f"{error}" for error in error_list)

    else:
        return f"{ticket} is valid."


# Testing
if __name__ == "__main__":
    print(validate_jira_ticket("HSU-123"))   # valid
    print(validate_jira_ticket("AB-9"))      # valid
    print(validate_jira_ticket("A-123"))     # not valid
    print(validate_jira_ticket("PROJECT-1")) # not valid
    print(validate_jira_ticket("PR-"))       # not valid


# Old validation
# if re.fullmatch(r"[A-Z]{2,5}-[0-9]{1,}", ticket):
#     return f"{ticket} is valid."
# else:
#     return f"{ticket} is not valid."