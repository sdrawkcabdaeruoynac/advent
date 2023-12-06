import junk
import re
text = open("/Users/zen/desktop/adventText.txt")

t_GAME = r"[0-9]+"
t_SETS = r"(\d+\s(red|blue|green)[,;\n]\s*)+"

records = []

match = {
   "GAME": str,
   "SETS": list,
   "POWER": int
}

color_checker = {
      "red": 0,
      "blue": 0,
      "green": 0
}

for y in text:
    game = re.search(t_GAME, y)
    match["GAME"] = game[0]
    sets = re.search(t_SETS,y)
    clean = re.split(r"[;\n]",sets[0])
    match["SETS"] = clean
    records.append(match.copy())

powerSum = 0
for item in records:

   bad_set = False
   game_sets = item["SETS"]

   for a_set in game_sets:

      split_sets_evenmore = re.findall(r"\d+|red|blue|green", a_set)

      while split_sets_evenmore and bad_set != True:

         color = split_sets_evenmore.pop()
         value = int(split_sets_evenmore.pop())

         if color_checker[color] < value:
            color_checker[color] = value
         print(item["GAME"],color_checker)

   powerSum = powerSum + color_checker["red"] * color_checker["blue"] * color_checker["green"]
   color_checker["red"] = color_checker["blue"] = color_checker["green"] = 0

print(powerSum)
