import re
#Jira Ticket Validator
# Validation conditions (Format: PROJECT-123)
# Project part = 2–5 uppercase letters, Dash (-), Number part = 1-4 digits

def validate_jira_ticket(ticket):
    if ticket.count("-") != 1:
        return "Ticket must contain exactly one hyphen."
    else:
        project, issue = ticket.split("-", 1)
        if not re.fullmatch(r"[A-Z]{2,5}", project):
            return "Jira project name must contain 2-5 uppercase letters."

        if not re.fullmatch(r"[0-9]{1,4}", issue):
            return "Jira issue must contain 1-4 digits."

    return f"{ticket} is valid."








