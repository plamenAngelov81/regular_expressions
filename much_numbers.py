import re

numbers = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

result = re.finditer(pattern, numbers)
print_list = []
for i in result:
    print_list.append(i.group())

print(" ".join(print_list))

