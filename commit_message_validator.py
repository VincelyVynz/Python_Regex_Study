import re
from jira_ticket_validator import validate_jira_ticket
#Commit message validator
# Format: <type>(<scope>): <subject> <JIRA-ID>
# Example: feature(auth): add login flow HSU-123

def commit_validator(message):
    types_list = ["feat", "feature", "fix", "bug", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"]
    colon_count = 0
    for char in message:
        if char  == ":":
            colon_count += 1

    if colon_count > 1:
        return "Only one colon allowed."

    elif colon_count == 0:
        return "Commit message must have one colon."

    else:
        type_scope, subject_jira_id = message.split(":")
        type_scope, subject_jira_id = type_scope.strip(), subject_jira_id.strip()

        if "(" not in type_scope:
            return "Invalid type scope."
        else:
            type_part,scope = type_scope.split("(",1)
            scope = scope.rstrip(")",1)
            if not re.fullmatch(r".+", scope):
                return "Missing scope."

            if type_part not in types_list:
                return "Invalid type."

        subject, jira_id = subject_jira_id.rsplit(" ",1)

        return subject, validate_jira_ticket(jira_id)





