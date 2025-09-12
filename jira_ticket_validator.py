import re
#Jira Ticket Validator

# Validation conditions (Format: PROJECT-123)
# Project part = 2–5 uppercase letters
# Dash (-)
# Number part = at least 1 digit

def validate_jira_ticket(ticket):

    if re.fullmatch(r"[A-Z]{2,5}-[0-9]{1,}", ticket):
        return f"{ticket} is valid"
    else:
        return f"{ticket} is not valid"