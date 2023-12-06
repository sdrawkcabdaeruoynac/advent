import junk
import re
text = open("/Users/zen/desktop/adventText.txt")

t_GAME = r"[0-9]+"
t_SETS = r"(\d+\s(red|blue|green)[,;\n]\s*)+"

records = []

match = {
   "GAME": str,
   "SETS": list,
   "POSSIBLE": bool
}

color_checker = {
      "red": 12,
      "blue": 14,
      "green": 13
}

for y in text:
    game = re.search(t_GAME, y)
    
    match["GAME"] = game[0]

    sets = re.search(t_SETS,y)
    clean = re.split(r"[;\n]",sets[0])

    match["SETS"] = clean

    records.append(match.copy())

winner = 0

for item in records:

   bad_set = False
   game_sets = item["SETS"]

   for a_set in game_sets:
      split_sets_evenmore = re.findall(r"\d+|red|blue|green", a_set)

      while split_sets_evenmore and bad_set != True:

         color = split_sets_evenmore.pop()
         value = int(split_sets_evenmore.pop())

         if int(color_checker[color]) < value:
            bad_set = True

      if bad_set == True:
         break

   if bad_set == False:
      print(item["GAME"])
      winner = winner + int(item["GAME"])

print(winner)

