import re
from jira_ticket_validator import validate_jira_ticket
#Commit message validator
# Format: <type>(<scope>): <subject> [JIRA-ID]
# Example: feature(auth): add login flow HSU-123

def commit_validator(message):
    message = message.strip()
    parts = re.match(r"^(?P<type_part>feat|feature|fix|bug|docs|style|refactor|perf|test|build|ci|chore|revert)"
                     r"\((?P<scope>[^)]+)\):\s*"
                     r"(?:"
                     r"(?P<jira_id1>\[[A-Z]{2,5}-[0-9]{1,4}\])\s*(?P<subject1>.+)"
                     r"|"
                     r"(?P<subject2>.+?)\s*(?P<jira_id2>\[[A-Z]{2,5}-[0-9]{1,4}\])"
                     r")$", message)


    if parts:
        result = {
        "type_part" : parts.group("type_part"),
        "scope" : parts.group("scope"),
        "subject" : parts.group("subject1") or parts.group("subject2"),
        "jira_id" : parts.group("jira_id1") or parts.group("jira_id2")
        }

        for name, value in result.items():
            if value is None:
                result[name] = "Missing or invalid."
            else:
                result[name] = value
            print(result)
    else:
        print("Missing or invalid format.")


# commit_validator("feature(auth): [HSU-123] add login flow ")
commit_validator("feature(auth): add login flow HSU-123 ")

# types_list = ["feat", "feature", "fix", "bug", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"]
# if message.count(":") != 1:
#     return "Commit message must contain exactly one colon."
#
# else:
#     type_scope, subject_jira_id = message.split(":",1)
#     type_scope, subject_jira_id = type_scope.strip(), subject_jira_id.strip()
#
#     if not ("(" in type_scope and type_scope.endswith(")")):
#         return "Invalid type scope."
#     else:
#         type_part,scope = type_scope.split("(",1)
#         scope = scope[:-1]
#         if not scope:
#             return "Missing scope."
#
#         if type_part not in types_list:
#             return "Invalid type."
#
#     if " " not in subject_jira_id:
#         return "Missing subject or jira ID."
#     else:
#         subject, jira_id = subject_jira_id.rsplit(" ",1)
#
#         jira_result = validate_jira_ticket(jira_id)
#         if  not jira_result.endswith("is valid."):
#             return jira_result
#
#
#     return f"Type: {type_part}\nScope: {scope}\nSubject: {subject}\nJira ID: {jira_id}\n{message} is a valid commit message"


