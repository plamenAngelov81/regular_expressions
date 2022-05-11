import re

text = input()
special_word = input()

reg = rf"\b{special_word}\b"

result = re.findall(reg, text, re.IGNORECASE)

print(len(result))
