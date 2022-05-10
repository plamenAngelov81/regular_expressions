import re

text = input()

pattern = r"([0-2][0-9]|3[01])([\.\/\-])([A-Z][a-z]+)\2(\d+)"

result = re.findall(pattern, text)

for i in result:
    print(f"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}")
    