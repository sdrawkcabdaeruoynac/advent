import re

text = open("/Users/zen/desktop/adventText.txt")
numbers = {
   "one" : '1',
   "two" : '2',
   "three": '3',
   "four" : '4',
   "five": '5',
   "six": '6',
   "seven": '7',
   "eight": '8',
   "nine": '9',
}

def getItemFromList(pos,list):
   if len(list[pos]) > 1:
      item = numbers.get(match[pos])
   else:
      item = match[pos]
   return item

sum = 0

for y in text:
   match = re.findall(r"[0-9]|one|two|three|four|five|six|seven|eight|nine",y)

   final = getItemFromList(0,match) + getItemFromList(len(match) - 1,match)

   sum = sum + int(final)

print(sum)
