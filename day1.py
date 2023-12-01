import re

def getItemFromList(pos,list):
   if len(list[pos]) > 1:
      item = numbers.get(match[pos])
   else:
      item = match[pos]
   return item

""" -------------------------------------- """

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

text = open("/Users/zen/desktop/adventText.txt")
sum = 0
part1 = "\d"
part2 = "\d|one|two|three|four|five|six|seven|eight|nine"

for y in text:
   match = re.findall(part2,y)
   sum = sum + int(getItemFromList(0,match) + getItemFromList(-1,match))
print(sum)
