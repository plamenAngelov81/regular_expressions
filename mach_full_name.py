import re

names = input()

match = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

matches = re.findall(match, names)

for i in matches:
    print(i, end=" ")

