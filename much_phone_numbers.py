import re

numbers = input()

reg = r"\+359([ -])2\1\d{3}\1\d{4}\b"

result = re.finditer(reg, numbers)

phones = []
for i in result:
    phones.append(i.group())

print(", ".join(phones))