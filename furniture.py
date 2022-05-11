import re

data = input()

money_spend = 0
furniture_list = []
pattern = r"^>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)$"
while True:
    if data == "Purchase":
        break
    match = re.search(pattern, data)
    if match:
        furniture = match[1]
        price = match[2]
        quantity = match[3]
        furniture_list.append(furniture)
        money_spend += float(price) * int(quantity)

    data = input()

print("Bought furniture:")

for i in furniture_list:
    print(i)

print(f"Total money spend: {money_spend:.2f}")
