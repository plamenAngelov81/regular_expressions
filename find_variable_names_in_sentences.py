import re

sentence = input()

pattern = r"\b_[a-zA-Z0-9]+\b"

result = re.findall(pattern, sentence)

printing_list = [x[1:] for x in result]

print(",".join(printing_list))
