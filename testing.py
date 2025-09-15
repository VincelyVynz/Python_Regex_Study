# ---------------------------- Testing commit messages ---------------------------- #

from commit_message_validator import commit_validator

print(commit_validator("feature(auth): add login flow HSU-123"))   # valid
print(commit_validator("fix(ui): resolve button alignment BUG-9")) # valid
print(commit_validator("docs(api): update README DOC-42"))         # valid
print(commit_validator("chore(build): update dependencies CI-7"))  # valid

print(commit_validator("featureauth): missing bracket HSU-123"))   # not valid (missing "(")
print(commit_validator("feature(auth: missing closing ) HSU-123")) # not valid (scope not closed)
print(commit_validator("feature(auth):missing space HSU-123"))     # valid (subject can start right away)
print(commit_validator("random(auth): add stuff HSU-123"))         # not valid (invalid type)
print(commit_validator("fix(auth): HSU-123"))                      # not valid (missing subject)
print(commit_validator("fix(auth): add patch HSU123"))             # not valid (invalid JIRA format)
print(commit_validator("fix(auth): add patch HSU-123-456"))        # not valid (too many hyphens in JIRA ID)
print(commit_validator("fix(auth): add patch H-1"))                # not valid (project too short)
print(commit_validator("fix(auth): add patch PROJECT-12345"))      # not valid (issue number too long)
print(commit_validator("feature(auth): add patch"))                # not valid (missing JIRA ID)


# ---------------------------- Testing jira tickets ---------------------------- #
from jira_ticket_validator import validate_jira_ticket

print(validate_jira_ticket("HSU-123"))   # valid
print(validate_jira_ticket("AB-9"))      # valid
print(validate_jira_ticket("A-123"))     # not valid
print(validate_jira_ticket("PROJECT-1")) # not valid
print(validate_jira_ticket("PR-"))       # not valid