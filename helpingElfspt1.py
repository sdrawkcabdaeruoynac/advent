import re

text = open("/Users/zen/desktop/adventText.txt")

sum = 0

for y in text:
   match = re.findall(r"\d",y)
   sum = sum + int( match[0] + match[-1])
print(sum)
