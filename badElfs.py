import junk
import re

matrix = []
digit_queue = []
item_postion = []

coordinates = {}

def main():

  with open("/Users/zen/desktop/adventText.txt") as text:
      for line in text:
          row = re.findall(r".",line)
          matrix.append(row.copy())

  for r in range(len(matrix)):
      for c in range(len(matrix[r])):
        coordinates[(r,c)] = matrix[r][c]

  for key in coordinates:
      if  coordinates[key] != '.':
       print(key, coordinates[key])


if __name__ == "__main__":
  main()
