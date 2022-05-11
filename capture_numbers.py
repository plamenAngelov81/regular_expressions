import re

text = input()
numbers = []

while text:
    matches = re.findall(r"\d+", text)
    numbers.extend(matches)
    text = input()

print(" ".join(numbers))

