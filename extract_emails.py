import re

text_data = input()

user_pattern = r"( |^)[a-zA-Z0-9]+([/.|\-|/_][a-zA-Z0-9]+)?"
host_pattern = r"([a-zA-Z0-9]+[\.|\-|\_])+[a-zA-Z0-9]+"
email = rf"{user_pattern}@{host_pattern}"
result = re.finditer(email, text_data)

for i in result:
    print(i.group())
