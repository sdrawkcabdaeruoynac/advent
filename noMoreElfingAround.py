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

sum = 0

for y in text:
   match = re.findall(r"[0-9]|one|two|three|four|five|six|seven|eight|nine",y)

   """check the first postion"""
   if len(match[0]) > 1:
      digit_one_str = numbers.get(match[0])
   else:
      digit_one_str = match[0]

   """check last position"""
   if len(match[len(match) - 1]) > 1:
      digit_two_str = numbers.get(match[len(match) - 1])
   else:
      digit_two_str = match[len(match) - 1]

   final = digit_one_str + digit_two_str

   sum = sum + int(final)

print(sum)
