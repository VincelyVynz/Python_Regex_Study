import re

text = "The cat chased another cat."

find_cat = re.findall(r"cat", text)
print(find_cat)