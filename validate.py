import re

email = input("Enter your email: ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid email")
else:
    print("Invalid email")