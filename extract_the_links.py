import re
pattern = r"((www)\.([a-zA-Z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
text = input()
urls = []
while text:
    matches = re.finditer(pattern, text)
    for i in matches:
        urls.append(i.group(1))
    text = input()

for x in urls:
    print(x)
