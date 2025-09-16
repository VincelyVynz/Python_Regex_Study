import re
# -------------------Commit message validator ------------------- #
# Format: <type>(<scope>): <subject> [JIRA-ID]
# Example: feature(auth): add login flow HSU-123

def commit_validator(message):
    message = message.strip()

    parts = re.match(r"^(?P<type_part>feat|feature|fix|bug|docs|style|refactor|perf|test|build|ci|chore|revert)?"
                     r"\((?P<scope>[^)]+)?\):\s*"
                     r"(?:"
                     r"(?P<jira_id1>\[[A-Z]{2,5}-[0-9]{1,4}\])\s*(?P<subject1>.+)?"
                     r"|"
                     r"(?P<subject2>.+?)\s*(?P<jira_id2>\[[A-Z]{2,5}-[0-9]{1,4}\])?"
                     r")$", message)


    if parts:

        result = {
        "type_part" : parts.group("type_part"),
        "scope" : parts.group("scope"),
        "subject" : parts.group("subject1") or parts.group("subject2"),
        "jira_id" : parts.group("jira_id1") or parts.group("jira_id2")
        }
        fully_valid = True
        for name, value in result.items():
            if value is None:
                print(f"❌{[name]} is missing or invalid.")
                fully_valid = False
            else:
                print(f"✅{name}:{value}")
        if fully_valid:
            print(f"{message} is a valid commit message.")
        else:
            print(f"{message} is not a valid commit message.")
    else:
        print("Missing or invalid format.")





