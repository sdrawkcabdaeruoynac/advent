import re

text = open("/Users/zen/desktop/adventText.txt")

sum = 0

for y in text:
   match = re.findall(r"\d",y)
   combine_digits = match[0] + match[ len(match) - 1]
   sum = sum + int(combine_digits)
print(sum)
